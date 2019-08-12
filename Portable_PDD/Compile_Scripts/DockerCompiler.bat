REM use Tectonic within a docker container to compile TeX to PDF
docker run --mount src="$(readlink -f $1)",target="/usr/src/tex",type=bind dxjoke/tectonic-docker tectonic $2