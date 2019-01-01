import xml.etree.ElementTree as xml
import os

ext_list = ['.mp4', '.mkv', '.avi', '.flv', '.mov', '.wmv', '.vob',
'.mpg','.3gp', '.m4v']		#List of extensions to be checked.

check_subdirectories = False		#Set false to get files only from cwd.

class Playlist:
	"""Build xml playlist."""
	
	def __init__(self):
	#Defines basic tree structure.
		self.playlist = xml.Element('playlist')
		self.tree = xml.ElementTree(self.playlist)
		self.playlist.set('xmlns','http://xspf.org/ns/0/')
		self.playlist.set('xmlns:vlc','http://www.videolan.org/vlc/playlist/ns/0/')
		self.playlist.set('version', '1')

		self.title = xml.Element('title')
		self.playlist.append(self.title)
		self.title.text = 'Playlist'

		self.trackList = xml.Element('trackList')
		self.playlist.append(self.trackList)

	def add_track(self, path):
	#Add tracks to xml tree (within trackList).
		track = xml.Element('track')
		location = xml.Element('location')
		location.text = path
		track.append(location)
		self.trackList.append(track)
	
	def get_playlist(self):
	#Return complete playlist with tracks.
		return self.playlist

class Videos:
	"""Manage files (videos) to be added to the playlist."""
	def __init__(self):
		pass

	def remove_nonvideo_files(self,file_list):
	#Removes files whose extension is not mentioned in ext_list from list of files.
		for index,file_name in enumerate(file_list[:]):
			#if file_name.endswith(tuple(ext_list)) or file_name.endswith(tuple(ext_list.upper())) :
			if file_name.endswith(tuple(ext_list)) or file_name.endswith(tuple(ext.upper() for ext in ext_list)):
				pass
			else:
				file_list.remove(file_name)
		return file_list
	
	def edit_paths(self, video_files):
	#Add path and prefix to files as required in vlc playlist file. 
		for index in range(len(video_files)):
			video_files[index] =( 
			'file:///' + os.path.join(video_files[index])).replace('\\','/')
		return video_files
	
	def get_videos(self):
	#Returns list of video files in the directory.
		if check_subdirectories == True:
			pathlist = [os.getcwd()]	#List of all directories to be scanned.
			for root, dirs, files in os.walk(os.getcwd()):
				for name in dirs:
						subdir_path = os.path.join(root, name)
						if subdir_path.find('\.') != -1:	#Excludes hidden directoriess.
							pass
						else:
							pathlist.append(subdir_path)
							
			videos = []
			#Loops through files of root directory and every subdirectory.
			for path in pathlist:
				all_files = os.listdir(path)
				for f in self.remove_nonvideo_files(all_files):
					location = path+ '\\' + f
					videos.append(location)
			return videos
			
		else:
			videos = []
			all_files = os.listdir()
			for f in self.remove_nonvideo_files(all_files):
					location = os.getcwd() + '\\' + f
					videos.append(location)
			return videos

def main():
	
	playlist = Playlist()
	videos = Videos()
	
	video_files = videos.get_videos()
	video_paths = videos.edit_paths(video_files)
	
	for path in video_paths:
		playlist.add_track(path)
	
	playlist_xml = playlist.get_playlist()
	with open('songs.xspf','w') as mf:
		mf.write(xml.tostring(playlist_xml).decode('utf-8'))
	
main()

'''
playlist(ROOT)
	title /title
	trackList
		track
			location file:///path /location
			title				  /title
			image				  /image
			duration			  /duration
		/track
	/tracklist
/playlist
'''
