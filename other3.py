from kivy.lang import Builder
from kivy.properties import StringProperty, ListProperty,ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition

from kivymd.app import MDApp
from kivymd.theming import ThemableBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import OneLineIconListItem,TwoLineIconListItem, MDList
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
import json

filename_members = "members.txt"
filename_ratelist = "ratelist.txt"

KV = '''
ScreenManager:
	LoginScreen:
	NavBar:



# Menu item in the DrawerList list.
<ItemDrawer>:
	theme_text_color: "Custom"
	on_release: self.parent.set_color_item(self)

	IconLeftWidget:
		id: icon
		icon: root.icon
		theme_text_color: "Custom"
		text_color: root.text_color


<ContentNavigationDrawer>:
	orientation: "vertical"
	
	spacing: "10dp"
	
	AnchorLayout:
		anchor_x: "left"
		size_hint_y: None
		height: avatar.height
		padding: "20dp"
		Image:
			id: avatar
			size_hint: None, None
			size: "56dp", "56dp"
			source: "data/logo/kivy-icon-256.png"

	MDLabel:
		text: "Raj Parihar"
		font_style: "Button"
		adaptive_height: True
		padding_x: "20dp"
		
	MDLabel:
		text: "RajParihar@gmail.com"
		font_style: "Caption"
		adaptive_height: True
		padding_x: "20dp"

	ScrollView:

		DrawerList:
			id:md_list
			OneLineIconListItem:
				text: "Add new member"
				on_press:
					root.nav_drawer.set_state("close")
					root.screen_manager.current = "signupscreen"
				IconLeftWidget:
					icon: "account-plus"
			
			OneLineIconListItem:
				id:tata1
				text: "Members"
				hide:True
				on_press:
					root.nav_drawer.set_state("close")
					root.screen_manager.current = "members"
				IconLeftWidget:
					icon: "account-details"
			OneLineIconListItem:
				id:tata2
				text: "inst"
				hide:True
				on_press:
					root.nav_drawer.set_state("close")
					root.screen_manager.current = "signupscreen"
				IconLeftWidget:
					icon: "users"

		
<LoginScreen>:
	name:'loginscreen'
	MDIcon:
		icon: 'account-key'
		icon_color: 0, 0, 0, 0
		halign: 'center'
		font_size: 100
		pos_hint: {'center_y':0.80}

	MDTextField:
		id:login_email
		size_hint : (0.7,0.1)
		hint_text: 'User Name'
		helper_text:'Required'
		helper_text_mode:  'on_error'
		icon_right: 'account-check'
		icon_right_color: app.theme_cls.primary_color
		required: True
		
		pos_hint: {'center_y':0.63,'center_x':0.5}

	MDTextField:
		id:login_password
		size_hint : (0.7,0.1)
		hint_text: 'Password'
		helper_text:'Required'
		helper_text_mode:  'on_error'
		icon_right: 'key-variant'
		icon_right_color: app.theme_cls.primary_color
		required: True
		
		pos_hint: {'center_y':0.50,'center_x':0.5}

	MDRaisedButton:
		text:'Login'
		size_hint: (0.13,0.07)
		pos_hint: {'center_y':0.37,'center_x':0.5}
		on_press:
			app.login()
			

<SignupScreen>:
	name:'signupscreen'
	MDIcon:
		icon: 'account-plus'
		icon_color: 0, 0, 0, 0
		halign: 'center'
		font_size: 90
		pos_hint: {'center_y':0.82}

	MDTextField:
		id:signup_username
		size_hint : (0.7,0.1)
		hint_text: 'Name'
		helper_text:'Required'
		helper_text_mode:  'on_error'
		icon_right: 'account'
		icon_right_color: app.theme_cls.primary_color
		required: True
		
		pos_hint: {'center_y':0.68,'center_x':0.5}

	MDTextField:
		id:signup_email
		size_hint : (0.7,0.1)
		hint_text: 'Email'
		helper_text:'Required'
		helper_text_mode:  'on_error'
		icon_right: 'email'
		icon_right_color: app.theme_cls.primary_color
		required: True
		
		pos_hint: {'center_y':0.57,'center_x':0.5}

	MDTextField:
		id:signup_mobile
		size_hint : (0.7,0.1)
		hint_text: 'Mobile'
		helper_text:'Required'
		helper_text_mode:  'on_error'
		icon_right: 'phone'
		icon_right_color: app.theme_cls.primary_color
		required: True
		
		input_filter: 'int'
		pos_hint: {'center_y':0.46,'center_x':0.5}
	
	MDTextField:
		id:signup_address
		size_hint : (0.7,0.1)
		hint_text: 'Address'
		icon_right: 'map'
		icon_right_color: app.theme_cls.primary_color
		
		pos_hint: {'center_y':0.35,'center_x':0.5}

	MDRaisedButton:
		text:'Signup'
		size_hint: (0.13,0.07)
		pos_hint: {'center_y':0.22,'center_x':0.5}
		on_press: app.signup()

	MDTextButton:
		text: 'Already have member'
		pos_hint: {'center_y':0.10,'center_x':0.5}
		on_press:
			root.manager.current = 'members'
			root.manager.transition.direction = 'left'
	
<Members>:
	name:'members'
	id:members
	MDLabel:
		text:'All Customers'
		font_style:'H4'
		halign:'center'
		pos_hint: {'center_y':0.82}

	ScrollView:
		size_hint_y: 0.78
		DrawerList:
			id: membersList


<Check@MDCheckbox>:
	group: 'group'
	size_hint: None, None
	size: dp(48), dp(48)

<CustomOneLineIconListItem>:
	on_press:
		app.pick_op_format(self.text)
		self.ids.tick.active = True

	Check:
		id: tick
		active: False
		pos_hint: {'x': .8, 'y': .1}




<PurchaseShell>:
	name: 'purchaseshell'
	on_enter:
		root.manager.transition.direction = 'right'
	MDBoxLayout:	
		orientation: 'vertical'
		spacing: dp(10)
		padding: dp(20)

		MDBoxLayout:
			adaptive_height: True

			MDIconButton:
				icon: 'magnify'

			MDTextField:
				id: search_field
				hint_text: 'Search icon'
				on_text: app.gen_op_list(self.text, True)

	
		RecycleView:
			id: rv
			key_viewclass: 'viewclass'
			key_size: 'height'

			RecycleBoxLayout:
				padding: dp(10)
				default_size: None, dp(48)
				default_size_hint: 1, None
				size_hint_y: None
				height: self.minimum_height
				orientation: 'vertical'

   
<NavBar>:
	name: 'application'
	MDScreen:
		MDToolbar:
			id: toolbar
			pos_hint: {"top": 1}
			elevation: 10
			title: "Milk Dairy App"
			left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]

		MDNavigationLayout:
			ScreenManager:
				id: screen_manager
				SignupScreen:
				Members:
					id:members
				PurchaseShell:
					id:purchaseshell
			   
			MDNavigationDrawer:
				id: nav_drawer

				ContentNavigationDrawer:
					id: content_drawer
					screen_manager: screen_manager
					nav_drawer: nav_drawer

'''



full_ext= ['bmp', 'dib', 'eps', 'gif', 'icns', 'ico', 'im', 'jpeg', 
		   'tga', 'tiff', 'webp', 'xbm']


class LoginScreen(Screen):
	pass
class SignupScreen(Screen):
	pass
class NavBar(Screen):
	pass
class Members(Screen):
	pass
class PurchaseShell(Screen):
	pass
sm = ScreenManager(transition=FadeTransition())
sm.add_widget(LoginScreen(name = 'loginscreen'))
sm.add_widget(SignupScreen(name = 'signupscreen'))
sm.add_widget(NavBar(name = 'application'))
sm.add_widget(Members(name = 'members'))
sm.add_widget(PurchaseShell(name = 'purchaseshell'))

class ContentNavigationDrawer(MDBoxLayout):
	screen_manager = ObjectProperty()
	nav_drawer = ObjectProperty()
	pass


class TwoLineIconListItem(TwoLineIconListItem):
	icon = StringProperty()
	text_color = ListProperty((0, 0, 0, 1))


class CustomOneLineIconListItem(OneLineIconListItem):
	icon = StringProperty()


class DrawerList(ThemableBehavior, MDList):
	def set_color_item(self, instance_item):
		for item in self.children:
			if item.text_color == self.theme_cls.primary_color:
				item.text_color = self.theme_cls.text_color
				break
		instance_item.text_color = self.theme_cls.primary_color


class MilkApp(MDApp):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.output_ext=''

	def build(self):
		self.theme_cls.primary_palette = "Blue"
		self.badgespage = Builder.load_string(KV)
		return self.badgespage
		
	def debug(self):
		self.login_check= True
		self.redirect_page("purchaseshell")

	def on_start(self):
		self.login_check= False
		self.alluser()
		print(self.badgespage.get_screen("application").ids.screen_manager.get_screen("purchaseshell").ids.rv)
		self.gen_op_list()
		self.debug()
	
	def allMembersList(self):
		self.badgespage.get_screen("application").ids.members.ids.membersList.clear_widgets()
		for key in self.allUser:
			if key !="admin":
				self.badgespage.get_screen("application").ids.members.ids.membersList.add_widget(
					TwoLineIconListItem(icon="account",text=f"{self.allUser[key]['UserName']}",secondary_text=f"{key}")
				)

	def flash(self,msgtype, msgtext):
		cancel_btn_username_dialogue = MDFlatButton(text = 'Retry',on_release = self.close_username_dialog)
		self.dialog = MDDialog(title = msgtype,text = msgtext,size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
		self.dialog.open()

	def alluser(self):
		f = open(filename_members,"r")
		fileData = f.read()
		jsonData = json.loads(fileData) if (fileData != "") else {}
		f.close()
		self.allUserLen = len(jsonData)-1
		self.allUser = jsonData
		return jsonData


	def save_to_json(self,mobile, signup, checkonly):
		jsonData = self.alluser()
		if mobile in jsonData:
			if checkonly:
				return jsonData[mobile]
			else:
				return False
		else:
			if not checkonly:
				r= open(filename_members,"w")
				jsonData[mobile]= signup
				self.allUserLen = len(jsonData)
				self.allUser = jsonData
				self.allMembersList()
				r.write(json.dumps(jsonData))
				r.close()
				return True
			else:
				return False
		

	def signup(self):
		signupEmail = self.badgespage.get_screen("application").ids.screen_manager.get_screen('signupscreen').ids.signup_email.text
		signupMobile = self.badgespage.get_screen("application").ids.screen_manager.get_screen('signupscreen').ids.signup_mobile.text
		signupUsername = self.badgespage.get_screen("application").ids.screen_manager.get_screen('signupscreen').ids.signup_username.text
		signupAddress = self.badgespage.get_screen("application").ids.screen_manager.get_screen('signupscreen').ids.signup_address.text
		if signupEmail.split() == [] or signupMobile.split() == [] or signupUsername.split() == []:
			self.flash('Required Input', 'Please check required input')
		else:
			signup_info = {"Email":signupEmail,"UserName":signupUsername, "Address":signupAddress}
			if not self.save_to_json(signupMobile, signup_info, False):
				self.flash('Already Exist','Mobile no '+signupMobile+'\nAlready exist.')				
			else:
				self.redirect_page("members")
	
	def login(self):
		loginEmail = self.badgespage.get_screen('loginscreen').ids.login_email.text
		loginPassword = self.badgespage.get_screen('loginscreen').ids.login_password.text
		authentication =  self.save_to_json(loginEmail, loginPassword, True)
		if not authentication:
			self.flash('Incorrect Credentials',"User no longer exists.")
		else:
			if authentication["Address"] == loginPassword:
				self.login_check=True
				self.redirect_page("members")
			else:
				self.flash('Incorrect Credentials',"Password not match.")
	
	def gen_op_list(self, text="", search=False):
		def add_icon_item(format):
			self.badgespage.get_screen("application").ids.screen_manager.get_screen("purchaseshell").ids.rv.data.append(
				{
					"viewclass": "CustomOneLineIconListItem",
					"text":format,
				}
			)
		self.badgespage.get_screen("application").ids.screen_manager.get_screen("purchaseshell").ids.rv.data = []
		for format in full_ext:
			if search:
				if text in format:
					add_icon_item(format)	   
			else:
				add_icon_item(format)

		
	def close_username_dialog(self,obj):
		self.dialog.dismiss()
	
	def top_menu_call(self):
		self.menu.open()

	def pick_op_format(self, format):
		self.output_ext= format
		print(self.root.ids)

	def convert(self):
		print('okay', self.output_ext)


	def redirect_page(self, pageName):
		if self.login_check:
			self.badgespage.get_screen('application').manager.current = 'application'
			self.badgespage.get_screen("application").ids.screen_manager.get_screen(pageName).manager.current = pageName
			# self.badgespage.get_screen('application').ids.username_info.text = f"our Customers {self.allUserLen}"
		else:
			self.badgespage.get_screen('loginscreen').manager.current = 'loginscreen'
		

if __name__ == '__main__':
	MilkApp().run()