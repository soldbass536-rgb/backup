from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
import os, zipfile, requests, glob

# ⚠️ غيّر هذا الرقم إلى IP هاتفك (جهاز الاستقبال)
SERVER_IP = "192.168.43.120"
PORT = 8080

class BackupApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        self.label = Label(text="اضغط الزر لإرسال الصور")
        btn = Button(text="ارسال النسخة الاحتياطية الآن")
        btn.bind(on_press=self.send_files)
        layout.add_widget(self.label)
        layout.add_widget(btn)
        return layout

    def send_files(self, instance):
        self.label.text = "جاري البحث عن الصور..."
        files_list = []
        folders = ["/sdcard/DCIM", "/sdcard/Pictures", "/sdcard/Download"]
        for f in folders:
            if os.path.exists(f):
                files_list.extend(glob.glob(f"{f}/**/*.jpg", recursive=True))
                files_list.extend(glob.glob(f"{f}/**/*.png", recursive=True))
                files_list.extend(glob.glob(f"{f}/**/*.pdf", recursive=True))

        if not files_list:
            self.label.text = "لا توجد ملفات!"
            return

        self.label.text = f"تم العثور على {len(files_list)} ملف، جاري الضغط..."
        zip_name = "backup.zip"
        with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as myzip:
            for file in files_list:
                myzip.write(file, os.path.basename(file))

        url = f"http://{SERVER_IP}:{PORT}"
        try:
            with open(zip_name, 'rb') as f:
                requests.post(url, data=f.read(), timeout=30)
            self.label.text = "✅ تم الإرسال بنجاح!"
        except:
            self.label.text = "❌ فشل الإرسال (تأكد من IP)"
        
        os.remove(zip_name)

if __name__ == "__main__":
    BackupApp().run()
