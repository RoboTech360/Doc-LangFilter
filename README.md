# Doc-LangFilter
Documentation Package Language Filter
Documentation Language Filter is a tool that removes non-English language folders from a documentation package. It is designed to simplify the process of filtering out directories containing languages other than English, leaving only the English version intact.

NOTE: Next major release will have option to select language folders to keep. 


Usage:

Download the executable file from the dist/ section.

Place the executable file in the root directory of the documentation package you want to filter.

Double-click on the executable file to run the tool. Select Option.

The tool will automatically scan through all subdirectories within the root directory and remove any non-English language folders.

After the tool finishes running, you will find that only the English language folder(s) remain in the documentation package.


Notes:
Make sure to back up your documentation package before using this tool to avoid permanent data loss.

The tool assumes that the English language folder is labeled "EN". If your documentation package uses a different naming convention, please rename the English folder accordingly.

This tool is provided as-is without any warranty. Use it at your own risk.



PS: 
This tool was initially made to delete folders from ABB Robot IRC5 / IRC5P / Omnicore documentation packages, saving ~80% disk space. this is significant when user have to keep multiple revision on computer. 
feel free to commit changes to improve this tool. majority of equipment manual/ documentation contain multiple language directories using same 2 letter convention. 
