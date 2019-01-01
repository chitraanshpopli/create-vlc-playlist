# create-vlc-playlist

I have a folder in which I keep my video songs and save them as a VLC playlist. 
This program eliminates the need to create a new playlist everytime I add/remove video to/from the folder.
It on launch, automatically creates a VLC media player playlist (.xspf) containing all the videos in the working directory.
The video containers can be added or removed from the ext_list variable. Can be used for audio files also.

Note that compared to what VLC media player makes on using it's 'save as playlist' option,
this creates a very bare-bone xml structure, the minimum that I found necessary for the file to work. 
So the xspf file is ugly but it works.

Updated to automatically go through subdirectories as well. Can be disabled from within the program via the flag.

#### Known problems:
1. Files with '%' or '#' in their names get added to the playlist but generate error when played.
2. If a file's name starts with '#', the file selection is ruined. It adds all the files' (and subdirectories')
   to the playlist regardless to them being video or not.
