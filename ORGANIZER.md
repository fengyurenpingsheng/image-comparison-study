# 组织者说明：图像对比实验

这份说明给组织实验的人（你）看：怎么把实验发布到 GitHub、怎么发链接、怎么收结果。
参与者看的是网站上的图文教程 `guide.html`，不用看这份。

## 0. 总览

- 每位参与者用**自己的链接**做一套题。一共 24 套（P01–P24），每套 318 道正式题加 6 道练习，约 30 分钟。
- 目标：**16–24 份合格结果**。超过 24 人，可以从 P01 开始再发一轮。
- 先找 **2 位**（不是本研究作者的人）试做，先检查这 2 份结果（第 5 步），没问题再大规模发。
- 结果：参与者做完会下载一个 `.json` 文件发给你；也可以设置成自动提交（第 3 步）。
- 你把收到的文件都放进研究文件夹的 `subj_own_results/`，再运行分析（第 6 步）。

## 1. 发布到 GitHub（只做一次，约 10 分钟）

> 仓库已经建好、网站已经上传：<https://github.com/fengyurenpingsheng/image-comparison-study>。这一节留作以后重新发布时参考。

### 1.1 新建仓库

1. 登录 GitHub（fengyurenpingsheng），打开 <https://github.com/new>。
2. **Repository name** 填 `image-comparison-study`。
3. 选 **Public**（免费的 GitHub Pages 只支持公开仓库）。
4. **不要**勾选 "Add a README file"，其他选项也都不用选。
5. 点 **Create repository**。

### 1.2 把网站文件推送上去（Mac 终端）

先进入 `study_site` 文件夹：在终端里输入 `cd`（后面加一个空格），把 Finder 里的 `study_site` 文件夹拖进终端窗口，按回车。然后整段复制运行：

```bash
git init
git config user.name "Haisheng Fu"
git config user.email "35984224+fengyurenpingsheng@users.noreply.github.com"
git config http.postBuffer 524288000
git add .
git commit -m "Image comparison study"
git branch -M main
git remote add origin https://github.com/fengyurenpingsheng/image-comparison-study.git
git push -u origin main
```

- 一共约 180 MB，要几分钟。
- 邮箱用的是你 GitHub 账号自带的"不公开邮箱"（noreply），提交会记在你的账号下，贡献者只有你一个人。
- **如果提示输入用户名和密码**：GitHub 已经不接受账户密码了。最简单的办法是装 GitHub 命令行工具并登录一次：

  ```bash
  brew install gh
  gh auth login        # 依次选：GitHub.com → HTTPS → Yes → Login with a web browser，按提示在浏览器里确认
  git push -u origin main
  ```

### 1.3 打开 GitHub Pages（让它变成网站）

1. 打开仓库页面 <https://github.com/fengyurenpingsheng/image-comparison-study> → 上方 **Settings** → 左边栏 **Pages**。
2. **Build and deployment** 下的 **Source** 选 **Deploy from a branch**。
3. **Branch** 选 `main`，文件夹选 `/ (root)`，点 **Save**。
4. 等 1–3 分钟后刷新，页面上方会出现：Your site is live at <https://fengyurenpingsheng.github.io/image-comparison-study/>
5. 打开这个网址，自己随便选一个编号试做几题；再打开 <https://fengyurenpingsheng.github.io/image-comparison-study/guide.html> 看看教程。自己试的结果不用发。

## 2. 填写设置（config.js）

用文本编辑器打开 `study_site/config.js`，只改引号里的文字：

- `contact_zh` / `contact_en`：你的联系方式（例如邮箱或微信号）。参与者在说明页和结束页会看到，用来提问和发结果文件。
- `ethics_zh` / `ethics_en`：伦理审批批下来以后，填一句话和批准编号。
- `upload_url`：自动提交的地址，可选，见第 3 步；不用就留空。

改完推送（先像 1.2 那样进入 `study_site` 文件夹）：

```bash
git add config.js
git commit -m "Update settings"
git push
```

一两分钟后网站会更新（浏览器里按住 Shift 再点刷新）。

## 3. （可选）自动收集结果

不设置也完全可以：参与者会下载结果文件，再发给你。
想让结果自动存到你的 Google Drive，按 `collect/README.md` 做（约 10 分钟）。中国大陆访问不了 Google，那边的参与者还是会被提示发文件。

## 4. 找人、发链接

**参与者条件**：年满 18 岁；有带键盘的电脑，屏幕至少 1600×900；视力正常或矫正后正常；有 30 分钟安静时间；最好不是本研究的作者。

**每人一个编号**：同一个链接不要发给两个人（除非 24 套都发完了，再从 P01 开始第二轮）。建议记一张表：

| 编号 | 中文链接 | 英文链接 | 发给谁 | 发出日期 | 是否合格 |
|---|---|---|---|---|---|
| P01 | <https://fengyurenpingsheng.github.io/image-comparison-study/?p=P01> | <https://fengyurenpingsheng.github.io/image-comparison-study/?p=P01&lang=en> | | | |
| P02 | <https://fengyurenpingsheng.github.io/image-comparison-study/?p=P02> | <https://fengyurenpingsheng.github.io/image-comparison-study/?p=P02&lang=en> | | | |
| P03 | <https://fengyurenpingsheng.github.io/image-comparison-study/?p=P03> | <https://fengyurenpingsheng.github.io/image-comparison-study/?p=P03&lang=en> | | | |
| P04 | <https://fengyurenpingsheng.github.io/image-comparison-study/?p=P04> | <https://fengyurenpingsheng.github.io/image-comparison-study/?p=P04&lang=en> | | | |
| P05 | <https://fengyurenpingsheng.github.io/image-comparison-study/?p=P05> | <https://fengyurenpingsheng.github.io/image-comparison-study/?p=P05&lang=en> | | | |
| P06 | <https://fengyurenpingsheng.github.io/image-comparison-study/?p=P06> | <https://fengyurenpingsheng.github.io/image-comparison-study/?p=P06&lang=en> | | | |
| P07 | <https://fengyurenpingsheng.github.io/image-comparison-study/?p=P07> | <https://fengyurenpingsheng.github.io/image-comparison-study/?p=P07&lang=en> | | | |
| P08 | <https://fengyurenpingsheng.github.io/image-comparison-study/?p=P08> | <https://fengyurenpingsheng.github.io/image-comparison-study/?p=P08&lang=en> | | | |
| P09 | <https://fengyurenpingsheng.github.io/image-comparison-study/?p=P09> | <https://fengyurenpingsheng.github.io/image-comparison-study/?p=P09&lang=en> | | | |
| P10 | <https://fengyurenpingsheng.github.io/image-comparison-study/?p=P10> | <https://fengyurenpingsheng.github.io/image-comparison-study/?p=P10&lang=en> | | | |
| P11 | <https://fengyurenpingsheng.github.io/image-comparison-study/?p=P11> | <https://fengyurenpingsheng.github.io/image-comparison-study/?p=P11&lang=en> | | | |
| P12 | <https://fengyurenpingsheng.github.io/image-comparison-study/?p=P12> | <https://fengyurenpingsheng.github.io/image-comparison-study/?p=P12&lang=en> | | | |
| P13 | <https://fengyurenpingsheng.github.io/image-comparison-study/?p=P13> | <https://fengyurenpingsheng.github.io/image-comparison-study/?p=P13&lang=en> | | | |
| P14 | <https://fengyurenpingsheng.github.io/image-comparison-study/?p=P14> | <https://fengyurenpingsheng.github.io/image-comparison-study/?p=P14&lang=en> | | | |
| P15 | <https://fengyurenpingsheng.github.io/image-comparison-study/?p=P15> | <https://fengyurenpingsheng.github.io/image-comparison-study/?p=P15&lang=en> | | | |
| P16 | <https://fengyurenpingsheng.github.io/image-comparison-study/?p=P16> | <https://fengyurenpingsheng.github.io/image-comparison-study/?p=P16&lang=en> | | | |
| P17 | <https://fengyurenpingsheng.github.io/image-comparison-study/?p=P17> | <https://fengyurenpingsheng.github.io/image-comparison-study/?p=P17&lang=en> | | | |
| P18 | <https://fengyurenpingsheng.github.io/image-comparison-study/?p=P18> | <https://fengyurenpingsheng.github.io/image-comparison-study/?p=P18&lang=en> | | | |
| P19 | <https://fengyurenpingsheng.github.io/image-comparison-study/?p=P19> | <https://fengyurenpingsheng.github.io/image-comparison-study/?p=P19&lang=en> | | | |
| P20 | <https://fengyurenpingsheng.github.io/image-comparison-study/?p=P20> | <https://fengyurenpingsheng.github.io/image-comparison-study/?p=P20&lang=en> | | | |
| P21 | <https://fengyurenpingsheng.github.io/image-comparison-study/?p=P21> | <https://fengyurenpingsheng.github.io/image-comparison-study/?p=P21&lang=en> | | | |
| P22 | <https://fengyurenpingsheng.github.io/image-comparison-study/?p=P22> | <https://fengyurenpingsheng.github.io/image-comparison-study/?p=P22&lang=en> | | | |
| P23 | <https://fengyurenpingsheng.github.io/image-comparison-study/?p=P23> | <https://fengyurenpingsheng.github.io/image-comparison-study/?p=P23&lang=en> | | | |
| P24 | <https://fengyurenpingsheng.github.io/image-comparison-study/?p=P24> | <https://fengyurenpingsheng.github.io/image-comparison-study/?p=P24&lang=en> | | | |

**邀请消息模板**（微信或邮件，把链接换成对应编号的）：

> 你好！我在做一个关于图像压缩质量的小实验，想请你帮忙参加。大约 30 分钟，需要用电脑（带键盘，屏幕至少 1600×900，手机不行）。
> 你的专属链接：https://fengyurenpingsheng.github.io/image-comparison-study/?p=P01
> 打开后跟着页面提示做就行，第一次可以先看页面上的「图文教程」。做完点「提交结果」，把下载的文件发给我。中途可以休息，也可以关掉网页，之后用同一个浏览器打开同一个链接就能接着做。谢谢！

> Hi! I am running a short study on image compression quality and would be grateful if you could take part. It takes about 30 minutes on a computer (keyboard, screen of at least 1600×900; phones will not work).
> Your personal link: https://fengyurenpingsheng.github.io/image-comparison-study/?p=P01&lang=en
> Just follow the instructions on the page (there is an illustrated guide). At the end click "Submit the result" and send me the downloaded file. You can take breaks or close the page and continue later in the same browser. Thank you!

## 5. 收结果、检查

1. 把收到的 `.json` 文件都放进研究文件夹的 `subj_own_results/`（没有就新建）。
2. 想自己先看看合不合格（可选）：

   ```bash
   # 先进入 study_site 文件夹（同 1.2），再运行：
   python3 tools/check_results.py "../subj_own_results"
   ```

   每份结果一行，最后一列是结论：
   - **合格**：可以用。
   - **没做完**：请对方用同一个浏览器打开链接接着做。
   - **注意力检查不合格**或**答得太快**：这份不能用，可以把同一个编号发给另一个人补做。
   - **重复**：同一份结果收到了两次（比如既自动提交又发了文件），没关系，分析时会自动去掉。
3. 前 2 份试做结果到了，先检查一次，再大规模发链接。

## 6. 分析

结果放好以后运行分析：分析程序读取 `subj_own_results/` 里的结果，以及研究文件夹 `subj_own/` 里的答案表（不在这个仓库里），给出每个编码器人眼看来的等效码率和置信区间。

## 7. 常见问题

- **参与者说屏幕检查过不了**：让他看 `guide.html` 第 3 步（调浏览器缩放，或者全屏）。屏幕太小（比如 1366×768 的老笔记本）就只能换电脑。
- **参与者在国内，网页很慢**：GitHub 在国内有时慢。可以让他在仓库页面点 **Code → Download ZIP**（约 180 MB），解压后双击 `index.html`，在页面上选自己的编号来做；或者你把 `study_site` 文件夹压缩后用网盘发给他。
- **做到一半换了电脑**：进度保存在原来的浏览器里。换电脑只能用同一个编号从头做。
- **想修改实验**：只改 `config.js`。不要改 `trials.js` 和 `stim/`，否则和分析用的答案表对不上。

## 8. 注意

- **不要**把答案表（研究文件夹 `subj_own/` 里以 `_key.json` 结尾的文件）放进这个仓库。它记录了每张图是哪个编码器、哪个码率；放出去，参与者就能看到答案，研究内容也会提前公开。它在研究文件夹的 `subj_own/` 里，不在 `study_site/` 里。
- **伦理**：多数大学要求先通过伦理审查再收集数据，期刊也可能要求在论文里写明。批下来以后把编号填进 `config.js`。
- 仓库里只写了"图像压缩质量研究"，没有提论文的题目、方法和投稿的会议或期刊。
