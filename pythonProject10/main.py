import cv2
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.camera import Camera
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.graphics.texture import Texture
from kivy.uix.gridlayout import GridLayout
from PIL import Image as PILImage
from datetime import datetime
import pandas as pd


class SelfieApp( App ):
    def build(self):
        self.camera = Camera( play=True )
        self.camera.resolution = (640, 480)

        self.label = Label()

        self.capture_button = Button( text="Capture Selfie" )
        self.capture_button.bind( on_press=self.capture )

        self.quit_button = Button( text="Quit" )
        self.quit_button.bind( on_press=self.quit_app )

        self.username_entry = TextInput( hint_text="Username" )
        self.password_entry = TextInput( hint_text="Password", password=True )

        self.login_button = Button( text="Login" )
        self.login_button.bind( on_press=self.login )

        layout = BoxLayout( orientation="vertical" )
        layout.add_widget( self.camera )
        layout.add_widget( self.capture_button )
        layout.add_widget( self.label )
        layout.add_widget( self.quit_button )
        layout.add_widget( self.username_entry )
        layout.add_widget( self.password_entry )
        layout.add_widget( self.login_button )

        self.logged_in = False
        self.logged_user = ""

        return layout

    def login(self, instance):
        # Replace this with your actual authentication logic
        username = self.username_entry.text
        password = self.password_entry.text
        if username == "user" and password == "password":
            self.logged_in = True
            self.logged_user = username
            self.username_entry.disabled = True
            self.password_entry.disabled = True
            self.login_button.disabled = True
            popup = Popup( title="Success", content=Label( text="Logged in as {}".format( username ) ),
                           size_hint=(None, None), size=(400, 200) )
            popup.open()
        else:
            popup = Popup( title="Error", content=Label( text="Invalid credentials" ), size_hint=(None, None),
                           size=(400, 200) )
            popup.open()

    def capture(self, instance):
        if not self.logged_in:
            popup = Popup( title="Error", content=Label( text="You must be logged in to capture a selfie." ),
                           size_hint=(None, None), size=(400, 200) )
            popup.open()
            return

        self.camera.export_to_png( "selfie.png" )
        selfie_filename = f"{self.logged_user}_{datetime.now().strftime( '%Y-%m-%d_%H-%M-%S' )}.jpg"
        cv2.imwrite( selfie_filename, cv2.imread( "selfie.png" ) )
        self.save_to_excel( self.logged_user, selfie_filename )
        popup = Popup( title="Success", content=Label( text="Selfie saved as '{}'".format( selfie_filename ) ),
                       size_hint=(None, None), size=(400, 200) )
        popup.open()

    def save_to_excel(self, username, selfie_filename):
        data = {
            "Username": [username],
            "Selfie Filename": [selfie_filename],
            "Timestamp": [datetime.now().strftime( '%Y-%m-%d %H:%M:%S' )],
        }
        df = pd.DataFrame( data )
        try:
            existing_data = pd.read_excel( "selfies.xlsx" )
            updated_data = pd.concat( [existing_data, df], ignore_index=True )
            updated_data.to_excel( "selfies.xlsx", index=False )
        except FileNotFoundError:
            df.to_excel( "selfies.xlsx", index=False )

    def quit_app(self, instance):
        self.camera.stop()
        App.get_running_app().stop()


if __name__ == "__main__":
    SelfieApp().run()
