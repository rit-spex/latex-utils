---
TITLE_TAG: 50\$ Satellite PDD
AUTHORS_TAG: Evan Putnam, Another Student 
EMAIL_TAG: emp9173@rit.edu, someOtherEmail@spex.com
TEMP_TAG: Hello World
---
<!--- 
    This is a template you can use for markdown with the SPEX PDD LaTeX documents.
    Specify a title, authors, and emails.

    Current Features:
        Sections
        Subsections
        Text and newlines.
        Basic LaTeX syntax (As long as no latex or regular comments are inside a statement).
    
    Commenting:
        Multiline comments are only supported if you have a single start and end on a seperate line.  For example you can not start a new comment on the same line as an ending tag for a multiline comment.  
        
        There can only be one single line comment per line.
        Nested comments are not supported.

    Important notes and potential gotchas:
        Comments.
        New lines.
--->

<!--- 
This is a special section that SHOULD exist.  
This is text for your abstract and should appear before other sections.
This CAN NOT have sub-sections and MUST have the # ABSTRACT syntax.
--->
# ABSTRACT
HERE BE A BIG HONKING ABSTRACT!

# Section 1
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

## Subsection 1.1
Hey how is it going?<!--- This is a single line comment which can be put anywhere!  Only one per line. --->

<!--- Completely blank lines are treated as a line break.--->
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
<!--- Comment lines are not.---> 
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

## Subsection 1.2
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.


# Section 2
Here is another section!

## Subsection 2.1
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

# Section 3
## Subsection 3.1
You can also include subsections where the section does not include text.


Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

# Section 4
## LaTeX Tables

<!--- You can use standard LaTeX syntax if it can be put on a single line. --->
This is a table \autoref{table:somechart}

<!--- 
This command counts as being on a single line.
Here is LaTeX code to create a table.
 --->
\begin{table}
  \centering
  \caption{Estimated Timeline}
  \begin{tabularx}{\columnwidth}{@{}cXl@{}} \toprule
    Phase & Task & Duration \\ \midrule
    1 & Review existing \$50SAT designs and materials & 2 weeks or less \\
    2 & Subsystem development & 6 weeks \\
      & Order PCB design and/or assembly & 6 weeks \\
      & Review changes to mechanical strucuture and order materials & 2 weeks or less \\
      & Testing of individual subsystems & 2 weeks \\
    3 & System Assembly & 1 week  \\
    4 & System testing & 2 weeks  \\
    5 & Generate documentation and delivery to SPEX & 1 week  \\
    \bottomrule
  \end{tabularx}
\label{table:somechart}
\end{table} \\

<!--- 
This command counts as being on a single line.
Here is an example of inserting an image in your document.
Image is one directory up of final folder so uses ../ formatting.
 --->
\begin{figure}[h]
 \centering
 \includegraphics[width=12cm, height=9cm]{../spex.png}
 \caption{Here is the SPEX Logo.}
\end{figure}
