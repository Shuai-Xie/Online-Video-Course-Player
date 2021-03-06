## Online Video Course Player

This is an **automatic** online video course player program, helping your finish the boring video-player-click work. Then you can enjoy your happy mahjong time!


Online video course: http://hnpi.newzhihui.cn/

---

### Dependencies
- selenium
- PIL
- tesserocr https://digi.bib.uni-mannheim.de/tesseract/

### Attention, Please!

- `chromedriver` is necessary. If you're using windows, you should [re-download](https://chromedriver.chromium.org/).


- `tesserocr` is used to recognize the **CAPTCHA** when logging in.


 ```sh
  ## Mac install tesserocr
  brew install tesseract
  CC=clang XCC=clang++ CPPFLAGS="-stdlib=libc++ -DUSE_STD_NAMESPACE -mmacosx-version-min=10.8" pip install tesserocr
  ```


- `this program` is very **Customized** as different online course webpages have different DOM architecture. But you can reference the solution and make it work on your scene.


- cutting to `./imgs/screen.png` can help tesserocr **locate the CAPTCHA in the login page**.


- a CAPTCHA sample

    ![](./imgs/checkCode.png)
    
logs...
```
重新登录...
重新登录...
重新登录...
重新登录...
重新登录...
登录成功!
total videos: 104
1, id: 20190819224123435797727455717560, title: 1-1 不忘初心继续前行一, progress:100%
2, id: 20190819224123439426122846264214, title: 2-1 焦裕禄精神1, progress:100%
3, id: 20190819224123438607991284231518, title: 2-2 焦裕禄精神2, progress:100%
4, id: 20190819224123438766285092424747, title: 2-3 焦裕禄精神3, progress:100%
5, id: 20190819224123441473464760962906, title: 3-1 红旗渠精神1, progress:100%
6, id: 20190819224123442393442352428734, title: 3-2 红旗渠精神2, progress:100%
7, id: 20190819224123441619509777322891, title: 3-3 红旗渠精神3, progress:100%
8, id: 20190819224123444982136885537511, title: 4-1 乡村振兴的总体策略及实施方案1, progress:100%
9, id: 20190819224123445846971490055943, title: 4-2 乡村振兴的总体策略及实施方案2, progress:100%
10, id: 20190819224123445239547823023587, title: 4-3 乡村振兴的总体策略及实施方案3, progress:100%
11, id: 20190819224123461565096666942423, title: 5-1 实施乡村振兴战略的重大意义1, progress:100%
12, id: 20190819224123461670521640914450, title: 5-2 实施乡村振兴战略的重大意义2, progress:100%
13, id: 20190819224123460705833462468480, title: 5-3 实施乡村振兴战略的重大意义3, progress:100%
14, id: 20190819224123464140339319270022, title: 6-1 实施乡村振兴战略的内容和要求1, progress:100%
15, id: 20190819224123464630706313891379, title: 6-2 实施乡村振兴战略的内容和要求2, progress:100%
16, id: 20190819224123464159261890313647, title: 6-3 实施乡村振兴战略的内容和要求3, progress:100%
17, id: 20190819224123467183286350058184, title: 7-1 实施乡村振兴战略的重点和举措1, progress:100%
18, id: 20190819224123468614762917436661, title: 7-2 实施乡村振兴战略的重点和举措2, progress:100%
19, id: 20190819224123467741878106550528, title: 7-3 实施乡村振兴战略的重点和举措3, progress:100%
20, id: 20190819224123471948804808939268, title: 8-1 乡村振兴战略的关键问题1, progress:100%
21, id: 20190819224123471264541695317229, title: 8-2 乡村振兴战略的关键问题2, progress:100%
22, id: 20190819224123470968609634587217, title: 8-3 乡村振兴战略的关键问题3, progress:100%
23, id: 20190819224123474483117032278278, title: 9-1 乡村振兴战略的体制机制1, progress:100%
24, id: 20190819224123475450165503872361, title: 9-2 乡村振兴战略的体制机制2, progress:100%
25, id: 20190819224123474241732063294723, title: 9-3 乡村振兴战略的体制机制3, progress:100%
26, id: 20190819224123478344799431462717, title: 10-1 乡村战略的总体思路1, progress:100%
27, id: 20190819224123477966323646475330, title: 10-2 乡村战略的总体思路2, progress:100%
28, id: 20190819224123478503886249239649, title: 10-3 乡村战略的总体思路3, progress:100%
29, id: 20190819224123481158995145537382, title: 11-1 乡村振兴战略的着力点1, progress:100%
30, id: 20190819224123482180832720522215, title: 11-2 乡村振兴战略的着力点2, progress:100%
31, id: 20190819224123481910737473045643, title: 11-3 乡村振兴战略的着力点3, progress:100%
32, id: 20190819224123484134994236586774, title: 12-1 精准扶贫基本要求1, progress:100%
33, id: 20190819224123485136095152444323, title: 12-2 精准扶贫基本要求2, progress:100%
34, id: 20190819224123485959911430965880, title: 12-3 精准扶贫基本要求3, progress:100%
35, id: 20190819224123488369298562917479, title: 13-1 精准扶贫的难点与思路1, progress:100%
36, id: 20190819224123488882648095360553, title: 13-2 精准扶贫的难点与思路2, progress:100%
37, id: 20190819224123489318766223475831, title: 13-3 精准扶贫的难点与思路3, progress:100%
38, id: 20190819224123492897745789783156, title: 14-1 推进生态文明建设美丽中国1, progress:100%
39, id: 20190819224123492505451162721539, title: 14-2 推进生态文明建设美丽中国2, progress:100%
40, id: 20190819224123492297504218430315, title: 14-3 推进生态文明建设美丽中国3, progress:100%
41, id: 20190819224123495424281361540456, title: 15-1 职业道德的要求和养成1, progress:100%
42, id: 20190819224123496841795927493364, title: 15-2 职业道德的要求和养成2, progress:100%
43, id: 20190819224123496826861795419721, title: 15-3 职业道德的要求和养成3, progress:100%
44, id: 20190819224123499159413732440151, title: 16-1 职业道德的基本规范1, progress:100%
45, id: 20190819224123499272268987499914, title: 16-2 职业道德的基本规范2, progress:100%
46, id: 20190819224123500161004900528941, title: 16-3 职业道德的基本规范3, progress:100%
47, id: 20190819224123502986241866657916, title: 17-1 职业道德概述1, progress:100%
48, id: 20190819224123503156035396014431, title: 17-2 职业道德概述2, progress:100%
49, id: 20190819224123503665936380242339, title: 17-3 职业道德概述3, progress:100%
50, id: 20190819224123511156528436965772, title: 18-1 生态文明和美丽中国建设一, progress:100%
51, id: 20190819224123511608959830850494, title: 18-2 生态文明和美丽中国建设二, progress:100%
52, id: 20190819224123514578137603847051, title: 19-1 新时代职业道德建设一, progress:100%
53, id: 20190819224123514756815839774493, title: 19-2 新时代职业道德建设二, progress:100%
54, id: 20190819224123542770273154776685, title: 20-1 不忘初心继续前行三, progress:100%
55, id: 20190819224123545831715090463153, title: 21-1 不忘初心继续前行四, progress:100%
56, id: 20190819224123547735801963257824, title: 22-1 不忘初心继续前行五, progress:100%
57, id: 20190819224123555211952436457144, title: 23-1 不忘初心二, progress:100%
58, id: 20190819224123558683557443518955, title: 24-1 大别山精神1, progress:100%
59, id: 20190819224123557558353564538787, title: 24-2 大别山精神2, progress:100%
60, id: 20190819224123558216487519386681, title: 24-3 大别山精神3, progress:100%
61, id: 20190819224123562477871227369822, title: 25-1 愚公移山1, progress:100%
62, id: 20190819224123562778478464147462, title: 25-2 愚公移山2, progress:100%
63, id: 20190819224123561941788909411116, title: 25-3 愚公移山3, progress:100%
64, id: 20190819224123565729301576661060, title: 26-1 现代化进程中的乡村文化建设1, progress:100%
65, id: 20190819224123565629454324957339, title: 26-2 现代化进程中的乡村文化建设2, progress:100%
66, id: 20190819224123566873654792122049, title: 26-3 现代化进程中的乡村文化建设3, progress:100%
67, id: 20190819224123570553208902551996, title: 27-1 坚持绿色发展建设美丽乡村1, progress:100%
68, id: 20190819224123569955081427674400, title: 27-2 坚持绿色发展建设美丽乡村2, progress:100%
69, id: 20190819224123569852445931763279, title: 27-3 坚持绿色发展建设美丽乡村3, progress:100%
70, id: 20190819224123573973029000569079, title: 28-1 我国特色小镇的功能与路径创新1, progress:100%
71, id: 20190819224123573827698805495498, title: 28-2 我国特色小镇的功能与路径创新2, progress:100%
72, id: 20190819224123573196009065797362, title: 28-3 我国特色小镇的功能与路径创新3, progress:100%
73, id: 20190819224123577483002215196510, title: 29-1 浅谈精准扶贫工作中的农村社会治理1, progress:100%
74, id: 20190819224123577604718547830575, title: 29-2 浅谈精准扶贫工作中的农村社会治理2, progress:100%
75, id: 20190819224123577660336759248613, title: 29-3 浅谈精准扶贫工作中的农村社会治理3, progress:100%
76, id: 20190819224123506903412365728631, title: 30-1 区块链, progress:100%
77, id: 20190819224123508343366912428413, title: 31-1 VR产业发展现状, progress:100%
78, id: 20190819224123518964528843310558, title: 32-1 中原文化的五大特征一, progress:100%
79, id: 20190819224123518907262082392465, title: 32-2 中原文化的五大特征二, progress:0%
找到 video!
开始播放!
```