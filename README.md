# List Uniquification

## Assigned: Wednesday, October 27, 2021
## Due: Wednesday, November 3, 2021

After cloning this repository to your computer, please take the following steps:

- Follow the instructions on the Proactive Programmers web site for this project
- Use the `cd` command to change into the directory for this repository.
- Change into the program directory by typing `cd datauniquifier`.
- Install the dependencies for the project by typing `poetry install`
- Run the program with the correct input file by typing:
  - `poetry run datauniquifier --approach listcomprehension --column 1 --data-file input/data.txt`
  - `poetry run datauniquifier --approach listcomprehension --column 0 --data-file input/data.txt`
  - Please note that the program will not work unless you add the required source code
  - You should run the program in all possible configurations for `--approach` and `--column`
  - You should also try to run the program with only the `--help` flag
  - What happens when you run the program but specify an incorrect file?
- Confirm that the program is producing the expected output
- Use a `docker run` command for your operating system to run GatorGrader
- Provide all of the required responses in the `writing/reflection.md` file
