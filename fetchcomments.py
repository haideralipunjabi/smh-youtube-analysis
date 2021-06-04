import os
VIDEO_LIST = ["https://www.youtube.com/watch?v=2A2NY29iQdI", "https://www.youtube.com/watch?v=ix68oRfI5Gw", "https://www.youtube.com/watch?v=vsTTXYxydOE", "https://www.youtube.com/watch?v=WQ8Xgp8ALFo", "https://www.youtube.com/watch?v=_7vPNcnYWQ4", "https://www.youtube.com/watch?v=u7JnoRy2vng", "https://www.youtube.com/watch?v=X9zXcnSXNF0", "https://www.youtube.com/watch?v=Puo6Vgcbxps", "https://www.youtube.com/watch?v=myO8fxhDRW0", "https://www.youtube.com/watch?v=B3CsOx5U9Gs", "https://www.youtube.com/watch?v=7zBrbdU_y0s&t=66s", "https://www.youtube.com/watch?v=8Au47gnXs0w", "https://www.youtube.com/watch?v=o5Cv9fvajrc", "https://www.youtube.com/watch?v=FycDx69px8U", "https://www.youtube.com/watch?v=IcjgrB9vTec", "https://www.youtube.com/watch?v=vtN4tkvcBMA", "https://www.youtube.com/watch?v=lPMg0dk1hFI", "https://www.youtube.com/watch?v=1de6fO-9ZDU", "https://www.youtube.com/watch?v=8cNeAOpR-Ws", "https://www.youtube.com/watch?v=c3LhK2SAusk", "https://www.youtube.com/watch?v=BuC1IiZBY_o", "https://www.youtube.com/watch?v=WuY2-OrT9ig"]

if os.path.exists("rawdata"):
    os.system("rm -rf rawdata")
    os.mkdir("rawdata")



for idx,link in enumerate(VIDEO_LIST):
    print(f"----Downloading {idx+1}----")
    vid = link.split('=')[1]
    os.system(f"youtube-comment-downloader --youtubeid {vid} --output rawdata/{vid}.json")
