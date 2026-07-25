from engines.video_engine import VideoEngine

engine = VideoEngine()

engine.initialize()

print("Video engine initiated successfully")

engine.play("media/test.mp4")