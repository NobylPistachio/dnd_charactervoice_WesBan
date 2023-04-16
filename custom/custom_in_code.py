from SpeechToTextToSpeech import *

Undertale_FallenDown_Main = """[bah<235,30>bah<235,25>bah<235,30>bah<235,25>bah<235,30>bah<235,25>bah<235,30>]
[bah<235,25>bah<235,30>bah<235,25>bah<235,30>bah<235,25>]
[bah<235,23>bah<235,21>bah<525,25>bah<235,21>bah<235,23>bah<235,28>bah<235,27>]
[bah<235,28>bah<235,30>bah<235,27>bah<235,23>]
 
[bah<235,30>bah<235,23>bah<235,30>bah<235,23>bah<235,30>bah<235,23>bah<235,30>]
[bah<235,22>bah<235,30>bah<235,22>bah<525,31>bah<235,30>bah<235,26>bah<235,30>]
[bah<235,26>bah<235,28>bah<235,30>bah<510,28>bah<510,26>bah<510,25>]"""

Undertale_FallenDown_Side = """[bah<235,14>bah<235,18>bah<235,21>bah<235,18>bah<235,21>bah<235,18>]
[bah<235,14>bah<235,18>bah<235,21>bah<235,18>bah<235,21>bah<235,18>]
[bah<235,11>bah<235,15>bah<235,18>bah<235,15>bah<235,18>bah<235,15>]
[bah<235,11>bah<235,15>bah<235,18>bah<235,15>bah<235,18>bah<235,15>]
[bah<235,07>bah<235,11>bah<235,14>bah<235,11>bah<235,14>bah<235,11>]
[bah<235,07>bah<235,10>bah<235,14>bah<235,10>bah<235,14>bah<235,10>]
[bah<235,14>bah<235,18>bah<235,21>bah<235,18>bah<235,21>bah<235,18>]
[bah<235,13>bah<235,16>bah<235,21>bah<235,16>bah<235,21>bah<235,16>]"""

text = """[s<1,20>]hey.[s<1,12>]eye[s<1,15>]just[s<1,20>]met[s<1,15>]you.[s<1,12>]and this[s<1,15>]is[s<1,24>]creh[eh<200,24>]e[s<1,20>]Z

[s<1,20>]but[s<1,24>]here's[s<1,25>]my[s<1,24>]numb[s<1,20>]ber.[s<1,20>]so[s<1,24>]call[s<1,22>]me may[s<1,20>]be
"""

still_alive = """[thih<200,32>sswaa<120,31>ssah<120,29>tray<200,29>ah<200,31>mmff]
[ay<200,22>mey<120,32>kkey<120,31>ngah<200,29>now<200,29>thiy<200,31>rr_<200>hxuw<400,27>gsuh<200,29>kkseh<200,22>ss]
[ih<200,22>ts<90>hxah<300,29>rd<90>tow<200,31>ow<350,32>ver<200,29>stey<200,26>tmay<300,27>sae<350,29>dih<120,22>sfae<120,22>]
[shaa<500,31>n_<1600>ae<120,32>peh<150,31>cher<120,29>say<150,29>eh<200,31>ns_<1600>wey<200,22>dow<200,32>waa<200,31>t]
[wey<200,29>mah<500,29>stbey<200,31>kah<500,27>zwey<200,29>kae<500,22>nn]
[fow<500,29>rthaa<200,31>gah<500,32>daa<200,29>vah<500,26>llaa<200,27>vah<200,29>ss]
[eh<200,22>kseh<120,27>pthaa<120,29>waa<200,30>ns<80>hxow<200,29>ar<200,27>deh<200,25>dd]
[bah<200,22>ther<200,23>snow<400,25>seh<400,30>nskray<200,30>ih<200,29>now<200,27>ver<200,25>eh<200,27>vriy<200,25>mih<200,25>s]
[tey<350,25>kwey<200,22>ll<20>jhah<200,23>stkiy<350,25>paw<350,30>ntray<200,32>ih<200,30>ntih<200,29>llwiy<200,27>rah<200,27>n]
[aw<200,29>tah<350,30>fkey<350,30>kae<200,32>ndthaa<200,34>say<200,35>eh<200,35>nsgeh<200,34>tsdah<350,32>nnae<200,30>nd]
[yx<20>uw<200,32>mey<200,34>kah<200,34>niy<350,32>tgah<350,30>nfow<250,27>rthaa<180,25>piy<180,27>pih<180,27>ll<20>hxow<200,30>]
[ar<350,29>stih<200,29>ll<20>ah<200,31>llay<500,31>vv]"""


def main(text):
    TextToSpeech_aeiou(text,'Still_Alive.wav')
    print("done")

if __name__ == "__main__":
    main(still_alive)