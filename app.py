from customtkinter import *
import os
from PIL import Image
import threading
from xml_reader import XML_Reader
from CTkMessagebox import CTkMessagebox
from time import sleep


class Gui():
    def __init__(self) -> None:
        self.app = CTk()
        self.app.geometry("380x200")
        self.app.title("XML Reader")

        self.app.resizable(height=False, width=False)

        self.bg = '#004B93'
        self.xml_reader = XML_Reader

        self.title = CTkLabel(
            self.app, 
            text="XML Reader", 
            font=("Arial", 22), 
            fg_color=self.bg,
            compound="left",
            width=380,
            height=40,   
        )

        self.info_directory = CTkLabel(
            self.app,
            text='Selecione o diretório',

        )
      

        self.search_label = CTkLabel(
            self.app, 
            text="Selecione o diretório", 
            font=("Arial", 18), 
            text_color='white',
            compound="center", 
        )

        self.entry_text = StringVar()
        self.entry = CTkEntry(
            master=self.app, 
            placeholder_text='selecione o diretório', 
            width=260, 
            height=30,
            textvariable=self.entry_text,
        )

        self.search_button = CTkButton(
            self.app,
            text="Procurar",
            width=50,
            corner_radius=5,
            command=self.selectFile,
           
            
        )
        self.search_button.place(x=295, y=90)

        self.run_button = CTkButton(
            self.app,
            text="Processar",
            width=50,
            corner_radius=5, 
            fg_color='#239b56',
            hover_color='#1d8348',
            command=self.run_process

        )    

        self.progress_bar = CTkProgressBar(
            master=self.app,
            orientation='horizontal',
            width=245,
            height=15,
            determinate_speed=10

        )
        self.progress_bar.set(0)
        
        self.title.place(x=0, y=0)

        self.info_directory.place(x=25, y=65)

        self.entry.place(x=25, y=90)

        self.run_button.place(x=25, y=150)

        self.progress_bar.place(x=110, y=156)

    
    def move_progress(self):
        steps = 10
        for i in range(steps + 1):
            value = (i * steps) / self.xml_reader
            self.progress_bar.set(value)
            sleep(2)


    def success_popup(self):
        self.msg = CTkMessagebox(
            title='XML Reader',
            message="Concluido!", 
            icon="check", 
            option_1="OK",
            width=300,
            height=200,
            sound=True
        )



    def selectFile(self):
        self.username = os.getlogin()
        self.directory_path = filedialog.askdirectory(
            title="Selecione o diretório onde estão localizados os arquivos .xml",
            mustexist=True,
            initialdir=f'C:/Users/{self.username}/Desktop'
        )

        self.entry_text.set(self.directory_path)
    

    
    def saveFile(self):
        self.output_file = filedialog.asksaveasfilename(
            title='Selecione o diretório',
            defaultextension='.xlsx',
            filetypes=(('Excel Document', '.xlsx'), ('All Files', '*.*')),
            initialfile='EXPORT'
        )

        self.xml_reader.export_file(self.output_file)
        

    def run_xml_reader(self):
        # self.move_progress()

        self.xml_reader(self.directory_path).run()
        self.saveFile()
        self.success_popup()

        print(self.xml_reader.progress)
        
        

    def run_process(self):
        thr1 = threading.Thread(target=self.run_xml_reader, daemon=True)
        thr1.start()
        


    def run(self):
        self.app.mainloop()
        



if __name__ == '__main__':
    
    Gui().run()
