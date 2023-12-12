import gradio as gr
import msl

msl_log = msl.MSLLogparser("test/match/20190704_083452.A.msl")
msl_referee = msl.RefereeLog("test/match/20190704_083452.msl")
merge = msl.MergeLogs(referee_log=msl_referee, team_logs=[msl_log])

def greet(name):
    return "Hello " + name + "!"


demo = gr.Interface(fn=greet, inputs="text", outputs="text")

if __name__ == "__main__":
    demo.launch(show_api=False)