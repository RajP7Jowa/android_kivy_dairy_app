from kivy.lang import Builder
from kivy.properties import StringProperty, ListProperty,ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition

from kivymd.app import MDApp
from kivymd.theming import ThemableBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import OneLineListItem,TwoLineIconListItem, MDList
from kivymd.uix.button import MDFlatButton,MDRectangleFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.behaviors.toggle_behavior import MDToggleButton
from kivymd.uix.card import MDCardSwipe
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from functools import partial
from datetime import datetime
import json


filename_members = "./assets/members.txt"
filename_ratelist = "./assets/ratelist.txt"
filename_history = "./assets/history.txt"

KV = '''
ScreenManager:
	LoginScreen:
	NavBar:


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
		text: "Milk Shree Dairy"
		font_style: "Button"
		adaptive_height: True
		padding_x: "20dp"
		
	MDLabel:
		text: "Linga, Kareli"
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
				text: "Price List"
				hide:True
				on_press:
					root.nav_drawer.set_state("close")
					root.screen_manager.current = "pricelist"
				IconLeftWidget:
					icon: "view-list-outline"

			OneLineIconListItem:
				id:tata2
				text: "Purchase"
				hide:True
				on_press:
					root.nav_drawer.set_state("close")
					root.screen_manager.current = "purchasesell"
				IconLeftWidget:
					icon: "beer-outline"

		
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
		size_hint: (0.3,0.07)
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
		icon_right: 'email'
		icon_right_color: app.theme_cls.primary_color
		pos_hint: {'center_y':0.57,'center_x':0.5}

	MDTextField:
		id:signup_mobile
		size_hint : (0.7,0.1)
		hint_text: 'Identification'
		helper_text:'Required'
		helper_text_mode:  'on_error'
		icon_right: 'star'
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
		size_hint: (0.3,0.07)
		pos_hint: {'center_y':0.22,'center_x':0.5}
		on_press: app.signup()

	MDTextButton:
		text: 'Already have member'
		pos_hint: {'center_y':0.10,'center_x':0.5}
		on_press:
			root.manager.current = 'members'
			root.manager.transition.direction = 'left'

<SwipeToDeleteItem>:
	size_hint_y: None
	height: content.height

	MDCardSwipeLayerBox:
		padding: "8dp"
		MDIconButton:
			icon: "trash-can"
			pos_hint: {"center_y": .5}
			on_release: app.remove_customer(root.secondary_text)
			
	MDCardSwipeFrontBox:

		TwoLineListItem:
			id: content
			text: root.text
			secondary_text: root.secondary_text
			_no_ripple_effect: True
			

<Members>:
	name:'members'
	id:members
	MDLabel:
		text:'All Customers'
		font_style:'H5'
		halign:'center'
		pos_hint: {'center_y':0.82,'center_x':0.5}
		
	MDCard:
		padding: "10dp"
		size_hint: (0.8,0.75)
		pos_hint: {'center_x':0.5}
		orientation: "vertical"
		ScrollView:
			size_hint_y: 0.78
			MDList:
				id: membersList
				padding: 0

<Check@MDCheckbox>:
	group: 'group_customers'
	size_hint: None, None
	size: dp(30), dp(30)

<CustomOneLineIconListItem>:
	on_press:
		app.pick_op_format(self.text)
		self.ids.tick.active = True

	Check:
		id: tick
		active: False
		pos_hint: {'x': 0.8, 'y': .1}




<PurchaseSell>:
	name: 'purchasesell'
	on_enter:
		root.manager.transition.direction = 'right'
	MDLabel:
		text:'Purchase'
		font_style:'H4'
		halign:'center'
		pos_hint: {'center_y':0.82,'center_x':0.5}
	
	MDBoxLayout:	
		size_hint : (.75,0.1)
		spacing: dp(5)
		pos_hint: {'center_y':0.70,'center_x':0.5}
		orientation: 'vertical'
		MDBoxLayout:
			adaptive_height: True
			MDIconButton:
				icon: 'magnify'

			MDTextField:
				id: search_field
				hint_text: 'Search Customer'
				helper_text_mode:  'on_error'
				required: True
				on_text:
					app.menu_customer.dismiss()
					app.gen_op_list(self.text, True);app.menu_customer.open()
				on_focus:
					# if self.focus: app.menu_customer.open()
	
		RecycleView:
			id: rv
			key_viewclass: 'viewclass'
			key_size: 'height'
			RecycleBoxLayout:
				padding: dp(10)
				default_size: None, dp(35)
				default_size_hint: 1, None
				size_hint_y: None
				height: self.minimum_height
				orientation: 'vertical'

	MDGridLayout:
		size_hint : (1,0.1)
		pos_hint: {'center_y':0.58,'center_x':0.5}
		cols: 3
		MDBoxLayout:
			MDCheckbox:
				group: 'group_Timing'
				id: morning
				on_active: app.on_checkbox_active("timing","Morning",self.active)

			MDLabel:
				text: 'Morning'
				text_size: self.size
				valign: 'middle'

			MDCheckbox:
				group: 'group_Timing'
				id: evening
				on_active: app.on_checkbox_active("timing","Evening", self.active)

			MDLabel:
				text: 'Evening'
				text_size: self.size
				valign: 'middle'

		MDLabel:
			text: ' '
			text_size: self.size
			halign: 'center'
			size_hint : (0.3,0.1)

		MDBoxLayout:
			MDCheckbox:
				active: True
				group: 'group_cowBuffalo'
				id:cow
				on_active: app.on_checkbox_active("type","cow", self.active)

			MDLabel:
				text: 'Cow'
				text_size: self.size
				valign: 'middle'

			MDCheckbox:
				group: 'group_cowBuffalo'
				id: buffalo
				on_active: app.on_checkbox_active("type","buffalo", self.active)

			MDLabel:
				text: 'buffalo'
				text_size: self.size
				valign: 'middle'

	MDGridLayout:
		size_hint : (1,0.1)
		pos_hint: {'center_y':0.48,'center_x':0.5}
		cols: 2
		padding: dp(30),dp(0)
		spacing: dp(30),dp(10)
		MDTextField:
			id: field_snf
			hint_text: 'SNF'
			helper_text:'Required'
			helper_text_mode:  'on_error'
			required: True
			input_filter: 'float'
			on_focus: 
				app.assign_snf()
				if self.focus: app.menu_snf.open()

		MDTextField:
			id: field_cnf
			hint_text: 'FAT'
			helper_text:'Required'
			helper_text_mode:  'on_error'
			required: True
			input_filter: 'float'
			on_focus:
				app.assign_cnf()
				if self.focus: app.menu_cnf.open()

		MDTextField:
			id: field_litre
			hint_text: 'litre'
			helper_text:'Required'
			helper_text_mode:  'on_error'
			required: True
			input_filter: 'float'
			on_text: app.calculate_rate()

		MDTextField:
			id: field_price
			hint_text: 'Price'
			helper_text:'Required'
			helper_text_mode:  'on_error'
			required: True
			disabled:True
			text:"00.00"

	MDTextField:
		id: field_remark
		size_hint : (.75,0.1)
		hint_text: 'Remark'
		pos_hint: {'center_y':0.27,'center_x':0.5}
		on_focus: app.calculate_rate()

	MDRaisedButton:
		text:'Submit'
		id:purchase_submit
		size_hint: (0.3,0.07)
		pos_hint: {'center_y':0.17,'center_x':0.5}
		on_press: app.purchaseSumbit()

<PriceList>:
	name: 'pricelist'
	MDLabel:
		text:'Price List'
		font_style:'H4'
		halign:'center'
		pos_hint: {'center_y':0.82,'center_x':0.5}

	MDBoxLayout:
		pos_hint: {'center_y':0.75,'center_x':0.5}
		size_hint: (0.50,0.1)

		MDCheckbox:
			active: True
			group: 'group_cowBuffalo'
			id:cow_plist
			on_active: app.on_checkbox_pricelist("cow", self.active)

		MDLabel:
			text: 'Cow'
			text_size: self.size
			valign: 'middle'

		MDCheckbox:
			group: 'group_cowBuffalo'
			id: buffalo_plist
			on_active: app.on_checkbox_pricelist("buffalo", self.active)

		MDLabel:
			text: 'buffalo'
			text_size: self.size
			valign: 'middle'

	ScrollView:
		pos_hint: {'center_y':0.67,'center_x':0.5}
		size_hint: (0.8,0.07)
		orientation: "vertical"
		MDBoxLayout:
			adaptive_size: True
			id: tabs_price
		
	MDCard:
		padding: "10dp"
		size_hint: (0.8,0.63)
		pos_hint: {'center_x':0.5}
		orientation: "vertical"
		MDGridLayout:
			cols: 2
			padding: 0, root.height * 0.02
			size_hint_y: None
			size_hint_x: 1
			height: self.minimum_height
			MDLabel:
				text: 'FAT'
				text_size: self.size
				halign:'center'
			MDLabel:
				text: 'Price'
				text_size: self.size
				halign:'center'
		ScrollView:
			size_hint_y: 0.78
			orientation: "vertical"
			do_scroll_y: True
			do_scroll_x: False
			bar_width: 4
			MDGridLayout:
				id: pricelist_chart
				cols: 2
				padding: 0, root.height * 0.02
				size_hint_y: None
				size_hint_x: 1
				height: self.minimum_height

<NavBar>:
	name: 'application'
	MDScreen:
		MDToolbar:
			id:	 toolbar
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
				PurchaseSell:
					id:purchasesell
				PriceList:
					id:pricelist
				
			MDNavigationDrawer:
				id: nav_drawer

				ContentNavigationDrawer:
					id: content_drawer
					screen_manager: screen_manager
					nav_drawer: nav_drawer

'''



class LoginScreen(Screen):
	pass
class SignupScreen(Screen):
	pass
class NavBar(Screen):
	pass
class Members(Screen):
	pass
class PurchaseSell(Screen):
	pass
class PriceList(Screen):
	pass
sm = ScreenManager(transition=FadeTransition())
sm.add_widget(LoginScreen(name = 'loginscreen'))
sm.add_widget(SignupScreen(name = 'signupscreen'))
sm.add_widget(NavBar(name = 'application'))
sm.add_widget(Members(name = 'members'))
sm.add_widget(PurchaseSell(name = 'purchasesell'))
sm.add_widget(PriceList(name = 'pricelist'))

class ContentNavigationDrawer(MDBoxLayout):
	screen_manager = ObjectProperty()
	nav_drawer = ObjectProperty()
	pass

class MyToggleButton(MDRectangleFlatButton, MDToggleButton):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.background_down = self.theme_cls.primary_light
		self.font_color_down = [0.0, 0.0, 0.0, 0.87]
		
class TwoLineIconListItem(TwoLineIconListItem):
	icon = StringProperty()
	text_color = ListProperty((0, 0, 0, 1))


class SwipeToDeleteItem(MDCardSwipe):
	text = StringProperty()
	secondary_text = StringProperty()

class CustomOneLineIconListItem(OneLineListItem):
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
		self.output_ext_customer=''
		self.output_ext_snf=''
		self.output_ext_cnf=''
		self.output_ext_cow_buffalo="cow"
		self.pricelist_cowb_selection = "cow"
		

	def build(self):
		self.theme_cls.primary_palette = "Blue"
		self.badgespage = Builder.load_string(KV)
		return self.badgespage
		
	def debug(self):
		self.login_check= True
		self.redirect_page("purchasesell")

	def get_morning(self):
		hour_day = datetime.now().hour
		if (hour_day > 4) and (hour_day <= 12):
			self.badgespage.get_screen("application").ids.screen_manager.get_screen("purchasesell").ids.morning.active = True
		else:
			self.badgespage.get_screen("application").ids.screen_manager.get_screen("purchasesell").ids.evening.active = True

	def on_start(self):
		self.login_check= False
		
		self.badgespage.get_screen("application").ids.screen_manager.get_screen("purchasesell").ids.field_snf.disabled = True
		self.badgespage.get_screen("application").ids.screen_manager.get_screen("purchasesell").ids.field_cnf.disabled = True
		self.badgespage.get_screen("application").ids.screen_manager.get_screen("purchasesell").ids.field_litre.disabled = True
		self.badgespage.get_screen("application").ids.screen_manager.get_screen("purchasesell").ids.purchase_submit.disabled = True
		self.alluser()
		self.allMembersList()
		self.get_morning()
		self.gen_op_list()
		self.ratelist()
		self.pricelist_header()
		self.debug()
		# print(self.badgespage.get_screen("application").ids.members.ids.membersList)
	
	def allMembersList(self):
		self.badgespage.get_screen("application").ids.members.ids.membersList.clear_widgets()
		for key in self.allUser:
			if key !="admin":
				self.badgespage.get_screen("application").ids.members.ids.membersList.add_widget(
					SwipeToDeleteItem(text=f"{self.allUser[key]['UserName']}",secondary_text=f"{key}")
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

	def ratelist(self):
		f = open(filename_ratelist,"r")
		fileData = f.read()
		jsonData = json.loads(fileData) if (fileData != "") else {}
		f.close()
		self.rateListJson = jsonData
		return jsonData
		
	def get_history(self):
		f = open(filename_history,"r")
		fileData = f.read()
		jsonData = json.loads(fileData) if (fileData != "") else {}
		f.close()
		self.history = jsonData
		return True

	def writeOnfile(self, filename, dataOfJson):
		w= open(filename,"w")
		w.write(dataOfJson)
		w.close()
		return

	def save_to_json(self,mobile, signup, checkonly):
		jsonData = self.alluser()
		if mobile in jsonData:
			if checkonly:
				return jsonData[mobile]
			else:
				return False
		else:
			if not checkonly:
				jsonData[mobile]= signup
				self.allUserLen = len(jsonData)
				self.allUser = jsonData
				self.allMembersList()
				self.writeOnfile(filename_members, json.dumps(jsonData))
				return True
			else:
				return False

	def remove_customer(self, mobile):
		jsonData = self.alluser()
		del jsonData[mobile]
		self.allUserLen = len(jsonData)
		self.allUser = jsonData
		self.allMembersList()
		self.writeOnfile(filename_members, json.dumps(jsonData))
		

	def signup(self):
		signupEmail = self.badgespage.get_screen("application").ids.screen_manager.get_screen('signupscreen').ids.signup_email.text
		signupMobile = self.badgespage.get_screen("application").ids.screen_manager.get_screen('signupscreen').ids.signup_mobile.text
		signupUsername = self.badgespage.get_screen("application").ids.screen_manager.get_screen('signupscreen').ids.signup_username.text
		signupAddress = self.badgespage.get_screen("application").ids.screen_manager.get_screen('signupscreen').ids.signup_address.text
		if signupMobile.split() == [] or signupUsername.split() == []:
			self.flash('Required Input', 'Please check required input are missing.')
		else:
			signup_info = {"Email":signupEmail,"UserName":signupUsername, "Address":signupAddress}
			if not self.save_to_json(signupMobile, signup_info, False):
				self.flash('Already Exist','Identification no '+signupMobile+'\nAlready exist.')
			else:
				self.redirect_page("purchasesell")
	
	def login(self):
		loginEmail = self.badgespage.get_screen('loginscreen').ids.login_email.text
		loginPassword = self.badgespage.get_screen('loginscreen').ids.login_password.text
		authentication =  self.save_to_json(loginEmail, loginPassword, True)
		if not authentication:
			self.flash('Incorrect Credentials',"User no longer exists.")
		else:
			if authentication["Address"] == loginPassword:
				self.login_check=True
				self.redirect_page("purchasesell")
			else:
				self.flash('Incorrect Credentials',"Password not match.")
	
 
	def gen_op_list(self, text="", search=False):
		listOfMenu = []
		def add_icon_item(format, secondtext):
			listOfMenu.append(
				{
					"viewclass": "CustomOneLineIconListItem",
					"text": "[b] "+secondtext+" [/b][/size]"+ format
				}
			)
		for format in self.alluser():
			if format != "admin":
				if search:
					if text in self.allUser[format]['UserName']:
						add_icon_item(format, self.allUser[format]['UserName'])		
				else:
					add_icon_item(format, self.allUser[format]['UserName'])
		self.menu_customer = MDDropdownMenu(
			caller=self.badgespage.get_screen("application").ids.screen_manager.get_screen("purchasesell").ids.search_field,
			items=listOfMenu,
			position="bottom",
			width_mult=5,
			max_height=200 	 
		)
		
	def assign_snf(self):
		menu_items_snf = [
			{
				"viewclass": "OneLineListItem",
				"text": f"{i}",
				"on_release": lambda x=f"{i}": self.set_item(x,"snf"),
			} for i in self.rateListJson[self.output_ext_cow_buffalo]]
		self.menu_snf = MDDropdownMenu(
			caller=self.badgespage.get_screen("application").ids.screen_manager.get_screen("purchasesell").ids.field_snf,
			items=menu_items_snf,
			position="bottom",
			width_mult=5,
			max_height=200
		)
		self.menu_snf.bind(on_release=self.menu_callback)

	def menu_callback(self, instance_menu, instance_menu_item):
		print(instance_menu, instance_menu_item)


	def assign_cnf(self):
		menu_items_cnf = [
			{
				"viewclass": "OneLineListItem",
				"text": f"{i}",
				"on_release": lambda x=f"{i}": self.set_item(x,"cnf"),
			} for i in self.rateListJson[self.output_ext_cow_buffalo][self.output_ext_snf]]

		self.menu_cnf = MDDropdownMenu(
			caller=self.badgespage.get_screen("application").ids.screen_manager.get_screen("purchasesell").ids.field_cnf,
			items=menu_items_cnf,
			position="bottom",
			width_mult=5,
			max_height=200
		)
	

	def close_username_dialog(self,obj):
		self.dialog.dismiss()
	
	def top_menu_call(self):
		self.menu.open()

	def pick_op_format(self, format):
		self.badgespage.get_screen("application").ids.screen_manager.get_screen("purchasesell").ids.field_snf.disabled = False
		self.output_ext_customer= format.split("[/size]")[1]
		self.badgespage.get_screen("application").ids.screen_manager.get_screen("purchasesell").ids.search_field.text = (format.split("]")[1].split('[')[0]).strip()
		
	def set_item(self, text_item,type):
		if type =="snf":
			self.output_ext_snf = text_item
			self.badgespage.get_screen("application").ids.screen_manager.get_screen("purchasesell").ids.field_snf.text = text_item
			self.badgespage.get_screen("application").ids.screen_manager.get_screen("purchasesell").ids.field_cnf.disabled = False
			self.menu_snf.dismiss()
		if type =="cnf":
			self.output_ext_cnf = text_item
			self.badgespage.get_screen("application").ids.screen_manager.get_screen("purchasesell").ids.field_cnf.text = text_item
			self.badgespage.get_screen("application").ids.screen_manager.get_screen("purchasesell").ids.field_litre.disabled = False
			self.menu_cnf.dismiss()
	
	def calculate_rate(self):
		self.badgespage.get_screen("application").ids.screen_manager.get_screen("purchasesell").ids.purchase_submit.disabled = False
		rate = self.rateListJson[self.output_ext_cow_buffalo][self.output_ext_snf][self.output_ext_cnf]
		litre = self.badgespage.get_screen("application").ids.screen_manager.get_screen("purchasesell").ids.field_litre.text
		if rate !=0 and rate !="" and litre !="":
			self.badgespage.get_screen("application").ids.screen_manager.get_screen("purchasesell").ids.field_price.text =  str('{0:.3g}'.format(rate*float(litre)))
			
		
	def purchaseSumbit(self):
		bill_snf = ""
		bill_cnf = ""
		bill_customer = ""
		bill_cow_b = ""
		bill_litre = ""
		bill_price = ""
		if self.output_ext_snf != "" and self.output_ext_snf != 0:
			bill_snf = str(self.output_ext_snf)

		if self.output_ext_cnf != "" and self.output_ext_cnf != 0:
			bill_cnf = str(self.output_ext_cnf)
		
		if self.output_ext_customer != "" and self.output_ext_customer != 0:
			bill_customer = str(self.output_ext_customer)

		if self.output_ext_cow_buffalo != "" and self.output_ext_cow_buffalo != 0:
			bill_cow_b = self.output_ext_cow_buffalo
			
		litre = self.badgespage.get_screen("application").ids.screen_manager.get_screen("purchasesell").ids.field_litre.text
		if litre != "" and litre != 0:
			bill_litre = str(litre)

		bill_price = self.badgespage.get_screen("application").ids.screen_manager.get_screen("purchasesell").ids.field_price.text
		if bill_price != "" and bill_price != 0:
			bill_price = str(bill_price)
			
		if bill_snf != "" and bill_cnf != "" and bill_customer != "" and bill_cow_b != "" and bill_litre != "" and bill_price != "" and self.output_ext_timing !="":
			remark= self.badgespage.get_screen("application").ids.screen_manager.get_screen("purchasesell").ids.field_remark.text
			self.printSlip(bill_snf,bill_cnf, bill_customer,bill_cow_b, bill_litre, bill_price, remark, self.output_ext_timing)
		else:
			flash("Bill Generate","Something went wrong please try again later.")
		
	def printSlip(self, bill_snf,bill_cnf, bill_customer,bill_cow_b, bill_litre, bill_price, remark, sift):
		print(
			"sift >>>|"+ sift + 
			"bill_snf >>>| "+ bill_snf +
			"bill_cnf >>>| "+ bill_cnf +
			"bill_customer >>>| "+ bill_customer +
			"bill_cow_b >>>| "+ bill_cow_b +
			"bill_litre >>>| "+ bill_litre +
			"bill_price >>>| "+ bill_price
		)

		today = datetime.today()
		# Textual month, day and year	
		d2 = today.strftime("%a, %d %b %Y %I:%M %p")
		d3 = today.strftime("%a%d%b%Y%I%M%p")
		self.get_history()
		
		if bill_customer in self.history:
			self.history[bill_customer].insert(0,{d3:{"date":d2, "sift":sift,"type":bill_cow_b, "snf":bill_snf, "cnf":bill_cnf, "weight":bill_litre, "price":bill_price, "remark":remark}})
		else:
			self.history[bill_customer] = [{d3:{"date":d2, "sift":sift,"type":bill_cow_b, "snf":bill_snf, "cnf":bill_cnf, "weight":bill_litre, "price":bill_price, "remark":remark}}]
		self.writeOnfile(filename_history, json.dumps(self.history))


	def on_checkbox_active(self,type ,value, state):
		if type !="timing":
			if state:
				self.output_ext_cow_buffalo= value
		else:
			if state:
				self.output_ext_timing= value

	def pricelist_header(self):
		self.badgespage.get_screen("application").ids.screen_manager.get_screen("pricelist").ids.tabs_price.clear_widgets()
		self.ratelist()
		for i in self.rateListJson[self.pricelist_cowb_selection]:
			self.badgespage.get_screen("application").ids.screen_manager.get_screen("pricelist").ids.tabs_price.add_widget(MyToggleButton(text=f"{i}", group="tab_button", on_press=partial(self.on_loadPrice_list, f"{i}")))

	def on_loadPrice_list(self, *args, **kwargs):
		self.pricelist_snf_selection = (args[0])
		self.load_price_table()
   
	def on_checkbox_pricelist(self, value, state):
		if state:
			self.pricelist_cowb_selection = value
			self.pricelist_header()
			self.badgespage.get_screen("application").ids.screen_manager.get_screen("pricelist").ids.pricelist_chart.clear_widgets()

	def load_price_table(self):
		self.badgespage.get_screen("application").ids.screen_manager.get_screen("pricelist").ids.pricelist_chart.clear_widgets()
		for i in self.rateListJson[self.pricelist_cowb_selection][self.pricelist_snf_selection]:
			self.badgespage.get_screen("application").ids.screen_manager.get_screen("pricelist").ids.pricelist_chart.add_widget(MDLabel(text=f"{i}", halign="center"))
			self.badgespage.get_screen("application").ids.screen_manager.get_screen("pricelist").ids.pricelist_chart.add_widget(MDTextField(text=f"{self.rateListJson[self.pricelist_cowb_selection][self.pricelist_snf_selection][i]}", halign="center",helper_text='Required', helper_text_mode= 'on_error',required= True,input_filter= 'float',max_height=65,on_text_validate=partial(self.on_setPriceUpdate,f"{self.pricelist_cowb_selection}",f"{self.pricelist_snf_selection}", f"{i}" )))
	

	def on_setPriceUpdate(self, *args, **kwargs):
		cow_b= args[0]
		snf = args[1]
		cnf = args[2]
		price =args[3].text
		self.rateListJson[cow_b][snf][cnf] = price 
		self.writeOnfile(filename_ratelist, json.dumps(self.rateListJson))
		self.load_price_table()

	def redirect_page(self, pageName):
		if self.login_check:
			self.badgespage.get_screen('application').manager.current = 'application'
			self.badgespage.get_screen("application").ids.screen_manager.get_screen(pageName).manager.current = pageName
			# self.badgespage.get_screen('application').ids.username_info.text = f"our Customers {self.allUserLen}"
		else:
			self.badgespage.get_screen('loginscreen').manager.current = 'loginscreen'
		

if __name__ == '__main__':
	MilkApp().run()