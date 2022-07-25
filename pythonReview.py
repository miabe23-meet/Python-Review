def create_youtube_video(title,description):
	youtubeDictionary = {"title": title, "description" : description, "likes": 0, "dislikes":0, "comments": {}}
	return youtubeDictionary

def like(youtubeDictionary):
	if "likes" in youtubeDictionary:
		youtubeDictionary["likes"]=youtubeDictionary["likes"]+1
		return youtubeDictionary

def disLike(youtubeDictionary):
	if "dislikes" in youtubeDictionary:
		youtubeDictionary["dislikes"]=youtubeDictionary["dislikes"]+1
		return youtubeDictionary

def add_comment(youtubeDictionary,username,comment_text):
	youtubeDictionary["comments"][username]=comment_text
	return



