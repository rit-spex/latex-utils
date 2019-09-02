"""
Author: Evan Putnam
Description: This is a python file that converts basic markdown to a latex file based on a template.

TODO: Integrate some additional features.  See LatexMarkdownCompiler.compile() function.
TODO: Add additional logging beyond print statements.

The logic is not anything special and is just a state machine handling basic conditions.

SPEX Members are free to improve upon it as they see fit.
"""

import os
import sys
import re
import shutil
import logging
import argparse

# Possible regex for removing comments.
TEMPLATE_FILE = "spex_template.tex"
COMPILER = ".\\Compile_Scripts\\MikTexCompiler.bat"

#Template tags that exist inside the SPEX document.
ABSTRACT = "ABSTRACT_TAG"
SECTION_START = "SECTION_TAG"



#---------------------------------------------------------------------
# This is a class that handles the fine details of parsing and writing
# to a the new tex file for compilation.
#---------------------------------------------------------------------
class LatexMarkdownCompiler:

    #---------------------------------------------------------------------
    # Initialization requires path of markdown file, bath of script to 
    # to execute for compilation, as well as the name of the document.
    #---------------------------------------------------------------------
    def __init__(self, path_of_md_file, path_of_bat_script, document_name, tex_template_path, verbose=False):
        self.name = document_name
        self.md_path = path_of_md_file
        self.tex_template_path = tex_template_path
        self.bat_script = path_of_bat_script
        self.verbose = verbose

    #---------------------------------------------------------------------
    # Filters out comments from the markdown document.
    # Comments can exist multiline if they have no text before or after, 
    # or are a single line in the format of <!--- SOME TEXT --->.
    # Multiline comments must have starting and ending tags to themselves.
    #---------------------------------------------------------------------
    def _filter_out_comments(self):
        new_str = ""
        start_comment = False
        comment_balance = 0
        #Filter out commment lines and add regular text to the new str.
        with open(self.md_path) as md_file:
            for line in md_file.readlines():
                
                #If not a comment to regular string
                if "<!---" not in line and start_comment == False:
                    new_str += line

                #Here is the comment start.
                if "<!---" in line:
                    comment_balance += 1
                    start_comment = True
                    #Get everything before the comment and add it the line.
                    line_length = line.find("<!---")
                    remaining_text = line[0:line_length]
                    new_str += remaining_text
                    if "--->" not in line:
                        new_str += '\n'

                #Here is the comment end.
                if "--->" in line:
                    comment_balance -= 1
                    start_comment = False
                    #Find everything after the comment in that line.
                    line_length = line.find("--->")
                    remaining_text = line[line_length+len("--->"):]
                    new_str += remaining_text

        #Comments are malformed so this is an error.
        if start_comment == True or comment_balance != 0:
            print("***** ERROR: Malformed comments.  Can not parse the document. Please fix you comments to have a starting and ending tag." )
            print("In addition do NOT have <!--- or ---> anywhere in your markdown document that you do not expect a comment.")
            sys.exit(1)

        #Return markdown document text without markdown <!--- ---> comments
        return new_str


    #---------------------------------------------------------------------
    # Parses the markdown file text to form a data structure of the relevant
    # sections.  See the test.md for acceptable items.
    #---------------------------------------------------------------------
    def _parse(self):
        #Get markdown text without comments.
        markdown_file_str = self._filter_out_comments().split("\n")

        #Start metadata search bool
        start_metadata = False

        #Section storage
        current_section = None
        current_sub_section = None
        section_dict = {}

        tag_key_values = {}

        for line in markdown_file_str:
            #Start looking for metadata
            if line.startswith("---") and not start_metadata:
                start_metadata = True
                continue
            #Stop looking for metadata
            elif line.startswith("---") and start_metadata:
                start_metadata = False
                continue
            #If we are looking for metadata
            elif start_metadata:
                #Search for specific tags.
                line_parts = line.split(":")
                tag_key = line_parts[0].strip()
                tag_value = ":".join(line_parts[1:]).strip()
                tag_key_values[tag_key] = tag_value

            #Look at subsections
            else:
                #If start of section
                if line.startswith("#") and not line.startswith("##"):
                    current_sub_section = None
                    temp = "#"
                    current_section = line[line.find(temp) + len(temp):].strip()
                    section_dict[current_section] = {"text": "", "subsections":{}}
                    continue
                #If start of subsection
                elif line.startswith("##"):
                    #If we hit a subsection before a section, error out.
                    if current_section == None:
                        print("***** Error: Subsection before section")
                        print(line)
                        sys.exit(1)
                    #Else handle section
                    else:
                        s = "##"
                        current_sub_section = line[line.find(s) + len(s):].strip()
                        section_dict[current_section]["subsections"][current_sub_section] = ""
                        continue
                #Else
                else:
                    #If no subsection detected add to main section
                    if current_section != None and current_sub_section == None:
                        section_dict[current_section]["text"] += line
                        if line.strip() == "":
                            section_dict[current_section]["text"] += "\n"
                    #If main section detected and a subsection was detected.
                    elif current_section != None and current_sub_section != None:
                        section_dict[current_section]["subsections"][current_sub_section] += line
                        if line.strip() == "":
                            section_dict[current_section]["subsections"][current_sub_section] += "\n"
                    #If sections malformed this will hit and throw an error.
                    elif line.strip() != "":
                        print("***** Error: Malformed sections/subsections")
                        print(line)
                        sys.exit(1)
        if self.verbose:      
            #Print out wonderful information.
            print(section_dict)

        #Items that populate the spex_template.tex file
        return tag_key_values, section_dict

    #---------------------------------------------------------------------
    # Converts the markdown items to latex format and puts it into
    # featured tags in the spex_template.tex
    #---------------------------------------------------------------------
    def _latex_string(self, sections):

        #If no sections are detected then errors out.
        if len(sections) == 0:
            print("***** Error: No sections detected in your markdown file.")
            sys.exit(1)
        
        #If no abstract it errors out.  Shame on you...
        if "ABSTRACT" not in sections:
            print("----- Warning: No abstract in markdown.  Most documents should have an abstract.")
        if self.verbose:
            print(sections)

        #Storage for latex formatted strings for abstract and sections.
        abstract_str = ""
        sections_str = ""

        #Get abstract data
        if "ABSTRACT" in sections:
            for txt in sections["ABSTRACT"]["text"].split("\n"):
                if txt.strip() == "":
                    continue
                abstract_str += txt
                abstract_str += (r"\\") + ("\n")

        #Get section data
        for section in sections:
            if section == "ABSTRACT":
                continue
            else:
                #Get sections and section text
                sections_str += r"\section{" + section + "}\n"
                for txt in sections[section]["text"].split("\n"):
                    if txt.strip() == "":
                        continue
                    sections_str += txt
                    sections_str += (r"\\") + ("\n")
                
                #Get sub sections and sub section text.
                for sub_section in sections[section]["subsections"]:
                    sections_str += r"\subsection{" + sub_section + "}\n"
                    for txt in sections[section]["subsections"][sub_section].split("\n"):
                        if txt.strip() == "":
                            continue
                        sections_str += txt
                        sections_str += (r"\\") + ("\n")
                
        if self.verbose:
            #Prints out latex formatted strings.
            print(abstract_str)
            print("")
            print(sections_str)

        return abstract_str, sections_str
        

    #---------------------------------------------------------------------
    # Converts a markdown file to a .tex file and compiles it to a .pdf file.
    #   - First filters out comments
    #   - Second gets metadata information like title, author, emails.
    #   - Third it generates LaTeX for sections/subsections.
    #   - Fourth it puts the metadata and LaTeX code into a template PDD and saves off a new copy.
    #   - Fifth it runs whatever compile script that was given on bootup.
    #
    # Somewhere between or after the self._parse() call and the self._latex_string call 
    # there is opportunity to post process more if need be.  The following features would be good.
    #   - TODO: Include bold and italics
    #   - TODO: Include basic bullited lists.
    # For now users can default back to LaTeX tho and code has been provided in test.md for it.
    #---------------------------------------------------------------------
    def convert(self):
        #Get information needed for document
        tag_key_values, sections = self._parse()
        
        #Get latex formatted abstract and sections/subsections
        abstract_latex, sections_latex = self._latex_string(sections)
        
        #Read template latex file.
        tex_contents = ""
        with open(self.tex_template_path, "r") as fle:
            tex_contents = fle.read()
        
        #Replace template tags with relevant data.
        if abstract_latex != "":
            tex_contents = tex_contents.replace(ABSTRACT, abstract_latex)
        tex_contents = tex_contents.replace(SECTION_START, sections_latex)

        for key in tag_key_values:
            times_to_replace = tex_contents.count(key)
            for i in range(0, times_to_replace):
                tex_contents = tex_contents.replace(key, tag_key_values[key])

        if self.verbose:
            #Output complete LaTeX document.
            print("")
            print(tex_contents)
        
 
        #Get rid of directory so we can regenerate the new .tex file.
        if os.path.exists(self.name):
            shutil.rmtree(self.name)
        
        #Make a directory with the name of the document.
        os.mkdir(self.name)

        #Write latex file to new directory.
        tex_path = self.name+"\\"+self.name+".tex"
        with open(tex_path, "w") as fle:
            fle.write(tex_contents)
        
        return tex_path

    def compile(self, tex_path):
        #Compile the script.  System call is bat script, path of file, path of
        #folder that file exists in.  It compiles twice to fix fairly common issues with broken references in .aux file.
        for i in range(0, 2):
            os.system("%(compiler)s %(tex_dir)s %(tex_file)s" % {
                "compiler": self.bat_script,
                "tex_dir": self.name,
                "tex_file": ".\\" + tex_path
            })
        


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="converts basic markdown to TeX and PDF")
    parser.add_argument(
        "input",
        help="Path to source Markdown file to be converted."
    )
    parser.add_argument(
        "-c", "--compiler",
        help="Path to TeX->PDF compiler script. (Default: %s)" % COMPILER,
        required=False,
        default=COMPILER
    )
    parser.add_argument(
        "-o", "--output",
        help="File name of output TeX and PDF.",
        required=False
    )
    parser.add_argument(
        "-t", "--template",
        help="TeX template to use. (Default: %s)" % TEMPLATE_FILE,
        required=False,
        default=TEMPLATE_FILE
    )
    parser.add_argument(
        "--tex_only",
        help="Do not build the PDF after converting markdown->TeX.",
        required=False
    )
    parser.add_argument(
        "-v", "--verbose",
        help="Display additional information to the console.",
        action="store",
        required=False
    )
    args = parser.parse_args()

    if not args.output:
        document_name = os.path.splitext(args.input)[0]
    else: 
        document_name = args.output
    
    latex = LatexMarkdownCompiler(
        args.input, args.compiler, document_name, args.template, verbose=args.verbose)
    tex_path = latex.convert()
    if not args.tex_only:
        latex.compile(tex_path)
