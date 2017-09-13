# FailPrompt
Fail Prompt is a sad excuse for a command prompt. It sometimes doesn't want to do what you tell it.

## Commands
* instructions - Prints basic usage instructions
* ping - Prints `Pong!`
* matrix - Prints 1 million random digits to the console, as if you were looking at the internals of the matrix or something
* quit - Exits the program

## Adding New Commands
1. Create a function. Make it do whatever you want.
2. Add another entry in the `commands` dictionary. The key is what the user will type, and the value should be the function. Do not invoke the function, that is, do not put parentheses after the function name. Example: `"instructions": instructions`, not `"instructions": instructions()`. While it is not strictly required for functionality, please be sure to name commands according to what they do.
3. Add an entry to this readme file, in the Commands section above.