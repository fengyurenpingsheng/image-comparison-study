# 组织者说明：图像对比实验

这份说明给组织实验的人（你）看：怎么打开网站、怎么发链接、怎么收结果。
参与者看的是网站上的图文教程 `guide.html`，不用看这份。

## 0. 总览

- **所有人用同一个链接**：<https://fengyurenpingsheng.github.io/image-comparison-study/>（英文版在后面加 `?lang=en`）。
- 参与者在第一页填一个**名字、昵称或邮箱**，只用来区分结果，不会公开。题目顺序由网页自动安排（24 种打乱的顺序，按名字分配），不用你分配编号。
- 每人做 6 道练习和 119 道正式题（其中 6 道是注意力检查），约 15 分钟，中间休息 1 次。全部图片 64 张，约 31 MB。
- 目标：**15–20 份合格结果**，越多越好。先找 **2 位**（不是本研究作者的人）试做，检查没问题再大规模发。
- **内部编号**：检查脚本按开始时间给每份结果编号（#01、#02…）。论文和分析里只用编号，不用名字。
- 结果：参与者做完会下载一个 `.json` 文件发给你；也可以设置成自动提交（第 3 步）。

## 1. 打开网站（只做一次）

文件已经在仓库里：<https://github.com/fengyurenpingsheng/image-comparison-study>。还要打开 GitHub Pages：

1. 打开 <https://github.com/fengyurenpingsheng/image-comparison-study/settings/pages>。
2. **Build and deployment** 下的 **Source** 选 **Deploy from a branch**。
3. **Branch** 选 `main`，文件夹选 `/ (root)`，一定要点 **Save**。
4. 等 1–3 分钟后刷新，页面上方出现 "Your site is live at https://fengyurenpingsheng.github.io/image-comparison-study/" 就好了。
5. 自己打开网址试做几题（填一个测试名字，例如 `test`）；自己试的结果不用发。

## 2. 填写联系方式（config.js）

最简单的办法是直接在 GitHub 网页上改：

1. 打开 <https://github.com/fengyurenpingsheng/image-comparison-study/blob/main/config.js>，点右上角的铅笔图标（Edit）。
2. 只改引号里的文字：
   - `contact_zh` / `contact_en`：你的联系方式（例如邮箱）。参与者在说明页和结束页会看到，用来提问和发结果文件。
   - `ethics_zh` / `ethics_en`：伦理审批批下来以后，填一句话和批准编号。
   - `upload_url`：自动提交的地址，可选，见第 3 步；不用就留空。
3. 点 **Commit changes…**，再点 **Commit changes**。一两分钟后网站会更新（浏览器里按住 Shift 再点刷新）。

## 3. （可选）自动收集结果

不设置也完全可以：参与者会下载结果文件，再发给你。
想让结果自动存到你的 Google Drive，按 `collect/README.md` 做（约 10 分钟）。中国大陆访问不了 Google，那边的参与者还是会被提示发文件。

## 4. 找人、发链接

**参与者条件**：年满 18 岁；有带键盘的电脑，屏幕至少 1600×900；视力正常或矫正后正常；有 15 分钟安静时间；最好不是本研究的作者。

**邀请消息模板**（微信或邮件，所有人都发同一个链接）：

> 你好！我在做一个关于图像压缩质量的小实验，想请你帮忙参加。大约 15 分钟，需要用电脑（带键盘，屏幕至少 1600×900，手机不行）。
> 链接：https://fengyurenpingsheng.github.io/image-comparison-study/
> 打开后填一个名字或邮箱，跟着页面提示做就行，第一次可以先看页面上的「图文教程」。做完点「提交结果」，把下载的文件发给我。中途可以关掉网页，之后在同一台电脑上打开、填同样的名字就能接着做。谢谢！

> Hi! I am running a short study on image compression quality and would be grateful if you could take part. It takes about 15 minutes on a computer (keyboard, screen of at least 1600×900; phones will not work).
> Link: https://fengyurenpingsheng.github.io/image-comparison-study/?lang=en
> Type a name or e-mail on the first page and follow the instructions (there is an illustrated guide). At the end click "Submit the result" and send me the downloaded file. You can close the page and continue later on the same computer by typing the same name. Thank you!

## 5. 收结果、检查

1. 把收到的 `.json` 文件都放进研究文件夹的 `subj_own_results/`（没有就新建）。
2. 检查合不合格（可选）：在终端里输入 `cd`（后面加一个空格），把 `study_site_v2` 文件夹（或从 GitHub 下载 ZIP 解压出来的文件夹）拖进终端窗口，按回车，然后运行：

   ```bash
   python3 tools/check_results.py "../subj_own_results"
   ```

   每份结果一行：内部编号、名字、答题数、注意力检查、每题中位用时、总用时、屏幕，最后一列是结论：
   - **合格**：可以用。
   - **没做完**：请对方在同一台电脑上打开网页、填同样的名字接着做。
   - **注意力检查不合格**或**答得太快**：这份不能用，再找一个人补上。
   - **重复**：同一份结果收到了两次（比如既自动提交又发了文件），没关系，分析时会自动去掉。
   - 名字后面标 **同名**：两份结果填了同一个名字。可能是两个人碰巧同名（没关系），也可能是同一个人做了两次（只用先完成的那份）。
3. 前 2 份试做结果到了，先检查一次，再大规模发链接。

## 6. 分析

结果放好以后运行分析：分析程序读取 `subj_own_results/` 里的结果，以及研究文件夹 `subj_own/` 里第 2 版的答案表（不在这个仓库里），给出每个编码器人眼看来的等效码率和置信区间。

## 7. 常见问题

- **参与者说屏幕检查过不了**：让他看 `guide.html` 第 3 步（调浏览器缩放，或者全屏）。屏幕太小（比如 1366×768 的老笔记本）就只能换电脑。
- **参与者在国内，网页很慢**：可以让他在仓库页面点 **Code → Download ZIP**（约 35 MB），解压后双击 `index.html` 来做；或者你把 `study_site_v2` 文件夹压缩后用网盘发给他。
- **做到一半换了电脑**：进度保存在原来那台电脑的浏览器里。换电脑只能从头做（填同样的名字也可以）。
- **两个人填了同一个名字**：没关系，结果文件不会互相覆盖；检查脚本会标出「同名」。
- **想修改实验**：只改 `config.js`。不要改 `trials.js` 和 `stim/`，否则和分析用的答案表对不上。

## 8. 注意

- **不要**把答案表（研究文件夹 `subj_own/` 里以 `_key.json` 结尾的文件）放进这个仓库。它记录了每张图是哪个编码器、哪个码率；放出去，参与者就能看到答案，研究内容也会提前公开。
- **隐私**：结果文件里有参与者填的名字或邮箱，只保存在你自己的电脑里，不要放到公开的地方。论文里只用内部编号。
- **伦理**：多数大学要求先通过伦理审查再收集数据，期刊也可能要求在论文里写明。批下来以后把编号填进 `config.js`。
- 仓库里只写了"图像压缩质量研究"，没有提论文的题目、方法和投稿的会议或期刊。
