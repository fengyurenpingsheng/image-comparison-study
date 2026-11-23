/**
 * 自动收集实验结果（可选）/ Optional automatic collection of results
 *
 * 每份结果保存成你 Google Drive 里文件夹 image_study_results 中的一个 .json 文件。
 * Each result is saved as one .json file in the folder image_study_results of your Google Drive.
 * 设置步骤见 collect/README.md / Setup: see collect/README.md
 */
var FOLDER_NAME = 'image_study_results';

function doPost(e) {
  var lock = LockService.getScriptLock();
  lock.tryLock(15000);
  try {
    var body = (e && e.postData && e.postData.contents) ? e.postData.contents : '';
    if (!body || body.length > 5000000) return ContentService.createTextOutput('empty or too large');
    var it = DriveApp.getFoldersByName(FOLDER_NAME);
    var folder = it.hasNext() ? it.next() : DriveApp.createFolder(FOLDER_NAME);
    var stamp = new Date().toISOString().replace(/[:.]/g, '-');
    var name = 'image_study_unknown_' + stamp + '.json';
    try {
      var j = JSON.parse(body);
      var who = String((j && (j.pid || j.set)) || 'anon').replace(/[^A-Za-z0-9@._\-\u4e00-\u9fff]+/g, '_').slice(0, 40);
      if (j) name = 'image_study_' + who + '_' + String(j.started || stamp).replace(/[:.]/g, '-') + '.json';
    } catch (err) {
      name = 'image_study_unreadable_' + stamp + '.txt';
    }
    folder.createFile(name, body, MimeType.PLAIN_TEXT);
    return ContentService.createTextOutput('ok');
  } finally {
    lock.releaseLock();
  }
}

function doGet() {
  return ContentService.createTextOutput('ok: the collection address works');
}
