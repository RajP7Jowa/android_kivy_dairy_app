from kivy.lang import Builder
from kivy.properties import StringProperty, ListProperty,ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.metrics import dp
from kivymd.app import MDApp
from kivymd.theming import ThemableBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import OneLineListItem,TwoLineIconListItem, MDList,TwoLineAvatarIconListItem
from kivymd.uix.button import MDFlatButton,MDRectangleFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.behaviors.toggle_behavior import MDToggleButton
from kivymd.uix.card import MDCardSwipe
from kivymd.uix.label import MDLabel,MDIcon
from kivymd.uix.textfield import MDTextField
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.icon_definitions import md_icons
import copy
from datetime import datetime
import json
import os
import requests


filename_ratelist = "./assets/ratelist.txt"

KV = '''
ScreenManager:
	LoginScreen:
	NavBar:

<NavDrawerToolbar@Label>
	canvas:
		Line:
			points: self.x, self.y, self.x+self.width,self.y
			
<ContentNavigationDrawer>:
	orientation: "vertical"
	
	spacing: "10dp"
	
	BoxLayout:
		size_hint: (1, .4)
		NavDrawerToolbar:
			padding: 10, 10
			canvas.after:
				Color:
					rgba: (1, 1, 1, 1)
				RoundedRectangle:
					size: (self.size[1]-dp(14), self.size[1]-dp(14))
					pos: (self.pos[0]+(self.size[0]-self.size[1])/2, self.pos[1]+dp(7))
					source: "assets/logo.png"
	MDLabel:
		text: "Milk Shree"
		font_style: "Button"
		adaptive_height: True
		padding_x: "20dp"
		
	MDLabel:
		text: "Dairy"
		font_style: "Caption"
		adaptive_height: True
		padding_x: "20dp"

	ScrollView:
		do_scroll_x: False
		DrawerList:
			id:md_list
			OneLineIconListItem:
				size_hint: (1, 0.04)

			OneLineIconListItem:
				id:tata2
				text: "Purchase"
				hide:True
				on_press:
					root.nav_drawer.set_state("close")
					root.screen_manager.current = "purchasesell"
				IconLeftWidget:
					icon: "beer-outline"
			
			OneLineIconListItem:
				id:tata3
				text: "Setting"
				hide:True
				on_press:
					root.nav_drawer.set_state("close")
					root.screen_manager.current = "setting"
				IconLeftWidget:
					icon: "cog"



		
<Setting>:
	name:'setting'
	MDIcon:
		icon: 'cog'
		icon_color: 0, 0, 0, 0
		halign: 'center'
		font_size: 100
		pos_hint: {'center_y':0.80}

	MDTextField:
		id:settingpwd
		size_hint : (0.95,0.1)
		hint_text: 'Security Key'
		helper_text:'Required'
		helper_text_mode:  'on_error'
		icon_right: 'account-key'
		icon_right_color: app.theme_cls.primary_color
		required: True
		password:True
		pos_hint: {'center_y':0.50,'center_x':0.5}

	MDRaisedButton:
		text:'Access'
		size_hint: (0.5,0.07)
		pos_hint: {'center_y':0.37,'center_x':0.5}
		on_press:
			app.accessSetting()

<LoginScreen>:
	name:'loginscreen'
	MDIcon:
		icon: 'account'
		icon_color: 0, 0, 0, 0
		halign: 'center'
		font_size: 100
		pos_hint: {'center_y':0.80}

	MDTextField:
		id:login_email
		text:"admin"
		size_hint : (0.95,0.1)
		hint_text: 'User Name'
		helper_text:'Required'
		helper_text_mode:  'on_error'
		icon_right: 'account-check'
		icon_right_color: app.theme_cls.primary_color
		required: True
		pos_hint: {'center_y':0.63,'center_x':0.5}

	MDTextField:
		id:login_password
		size_hint : (0.95,0.1)
		hint_text: 'Password'
		helper_text:'Required'
		helper_text_mode:  'on_error'
		icon_right: 'key-variant'
		icon_right_color: app.theme_cls.primary_color
		required: True
		password:True
		pos_hint: {'center_y':0.50,'center_x':0.5}

	MDRaisedButton:
		text:'Login'
		size_hint: (0.5,0.07)
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
		size_hint : (0.95,0.1)
		hint_text: 'Name'
		helper_text:'Required'
		helper_text_mode:  'on_error'
		icon_right: 'account'
		icon_right_color: app.theme_cls.primary_color
		required: True
		
		pos_hint: {'center_y':0.68,'center_x':0.5}

	MDTextField:
		id:signup_email
		size_hint : (0.95,0.1)
		hint_text: 'Email'
		icon_right: 'email'
		icon_right_color: app.theme_cls.primary_color
		pos_hint: {'center_y':0.57,'center_x':0.5}

	MDTextField:
		id:signup_mobile
		size_hint : (0.95,0.1)
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
		size_hint : (0.95,0.1)
		hint_text: 'Address'
		icon_right: 'map'
		icon_right_color: app.theme_cls.primary_color
		
		pos_hint: {'center_y':0.35,'center_x':0.5}

	MDRaisedButton:
		text:'Add new customer'
		size_hint: (0.7,0.07)
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
	text: "T--"
	secondary_text: "--"
	# on_release: app.bill_history(root.secondary_text)
	IconLeftWidget:
		icon:"account"
	IconRightWidget:
		icon: "trash-can"
		on_press: app.remove_customer(root.secondary_text)
	
		

<Members>:
	name:'members'
	id:members
	MDLabel:
		text:'All Customers'
		font_style:'H5'
		halign:'center'
		pos_hint: {'center_y':0.85,'center_x':0.5}
		
	MDCard:
		padding: "10dp"
		size_hint: (1,0.80)
		pos_hint: {'center_x':0.5}
		orientation: "vertical"
		ScrollView:
			do_scroll_x: False
			size_hint_y: 0.1
			MDList:
				id: membersList
				padding: 0

<PurchaseSell>:
	name: 'purchasesell'
	on_enter:
		root.manager.transition.direction = 'right'
	MDLabel:
		text:'Purchase'
		font_style:'H5'
		halign:'center'
		pos_hint: {'center_y':0.85,'center_x':0.5}
	
	MDBoxLayout:	
		size_hint : (0.95,0.1)
		spacing: dp(5)
		pos_hint: {'center_y':0.75,'center_x':0.5}
		orientation: 'vertical'
		MDBoxLayout:
			adaptive_height: True
			MDTextField:
				id: search_field
				hint_text: 'Customer name'
				helper_text_mode:  'on_error'
				required: True
				on_text:app.pick_op_format()
	
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
		size_hint : (1,0.12)
		pos_hint: {'center_y':0.63,'center_x':0.5}
		cols: 2
		MDGridLayout:
			cols: 1
			MDLabel:
				text: ''
				size_hint : (1,0.1)
				valign: 'middle'
			MDGridLayout:
				cols: 2
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
				text: ''
				size_hint : (1,0.1)
				valign: 'middle'
			OneLineIconListItem:
				size_hint: (1, 0.01)


		MDBoxLayout:
			size_hint : (1,0.1)
			padding: dp(15),dp(0)
			MDTextField:
				id: field_snf
				hint_text: 'SNF'
				helper_text:'Required'
				helper_text_mode:  'on_error'
				required: True
				input_filter: 'float'
				on_focus: if self.focus: app.assign_snf()
					

	MDGridLayout:
		size_hint : (1,0.1)
		pos_hint: {'center_y':0.51,'center_x':0.5}
		cols: 2
		MDGridLayout:
			cols: 1
			MDLabel:
				text: ''
				size_hint : (1,0.1)
				valign: 'middle'
			MDGridLayout:
				cols: 2
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
					text: 'Buffalo'
					text_size: self.size
					valign: 'middle'	

		MDGridLayout:
			cols: 1
			padding: dp(15),dp(0)
			MDTextField:
				id: field_cnf
				hint_text: 'FAT'
				helper_text:'Required'
				helper_text_mode:  'on_error'
				required: True
				input_filter: 'float'
				on_focus: if self.focus: app.assign_cnf()

	MDGridLayout:
		size_hint : (1,0.1)
		pos_hint: {'center_y':0.39,'center_x':0.5}
		cols: 2
		padding: dp(30),dp(0)
		spacing: dp(30),dp(10)

		MDTextField:
			id: field_litre
			hint_text: 'litre'
			helper_text:'Required'
			helper_text_mode:  'on_error'
			required: True
			input_filter: 'float'
			on_focus: if self.focus: app.assign_litre()
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
		pos_hint: {'center_y':0.30,'center_x':0.5}

	MDRaisedButton:
		text:'Submit'
		id:purchase_submit
		size_hint: (0.3,0.07)
		pos_hint: {'center_y':0.19,'center_x':0.5}
		on_press: app.purchaseSumbit()

<PriceList>:
	name: 'pricelist'
	MDLabel:
		text:'Price List'
		font_style:'H5'
		halign:'center'
		pos_hint: {'center_y':0.85,'center_x':0.5}

	MDBoxLayout:
		pos_hint: {'center_y':0.79,'center_x':0.5}
		size_hint: (0.80,0.1)

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
			text: 'Buffalo'
			text_size: self.size
			valign: 'middle'
	
	MDBoxLayout:
		pos_hint: {'center_y':0.43,'center_x':0.5}
		ScreenManager:
			valign:"bottom"
			id: screen_manager_tab_price
			COWList:
				id:cowlist
			BUFFALOList:
				id:buffalolist
	
	
	

<COWList>:
	name:"cowlist"
	MDBoxLayout:
		pos_hint: {'center_y':0.75}
		size_hint: (1,0.15)
		MDTabs:
			background_color: [1,1,1,1]
			text_color_normal: [0,0,0,1]
			text_color_active: [0,0,1,1]
			id: tabs_cow
			on_tab_switch: app.on_tab_switch(*args)
	ScrollView:
		size_hint_y: 0.65
		pos_hint: {'center_y':0.40}
		orientation: "vertical"
		do_scroll_x: False

		MDGridLayout:
			id: pricelist_chart_cow
			spacing: dp(1),dp(20)
			padding: dp(50),dp(30)
			cols: 2
			size_hint_x: 1
			size_hint_y: None
			height: self.minimum_height
			

			
<BUFFALOList>:
	name:"buffalolist"
	MDBoxLayout:
		pos_hint: {'center_y':0.75}
		size_hint: (1,0.15)
		MDTabs:
			background_color: [1,1,1,1]
			text_color_normal: [0,0,0,1]
			text_color_active: [0,0,1,1]
			id: tabs_buffalo
			on_tab_switch: app.on_tab_switch(*args)
	
	ScrollView:
		size_hint_y: 0.65
		pos_hint: {'center_y':0.40}
		orientation: "vertical"
		do_scroll_x: False
		MDGridLayout:
			id: pricelist_chart_buffalo
			spacing: dp(1),dp(20)
			padding: dp(50),dp(30)
			cols: 2
			size_hint_x: 1
			size_hint_y: None
			height: self.minimum_height

	

<HistoryPage>:
	name: 'historypage'
	MDToolbar:
		title:'Demo'
		left_action_items:[['account',lambda x: app.redirect_page('members')]]
		elevation:0
		pos_hint: {"top": 0.90}
		md_bg_color: 1,1,1,1
		padding:0
		id:historypageCustomer
		specific_text_color:0,0,0,1
		size_hint_y: 0.08
		MDLabel:
			id:historypageCustomer1
			text_size: self.size
			valign: 'middle'
		
	MDBoxLayout:
		id:historypageDataTable
		size_hint: (1,0.82)
		pos_hint: {'center_x':0.5}
		orientation: "vertical"

<Content>
	name: 'printContent'
	orientation: "vertical"
	padding: dp(0),dp(0)
	spacing: dp(10),dp(10)
	size_hint_y: None
	height: "150dp"

<NavBar>:
	name: 'application'
	MDScreen:
		MDToolbar:
			id:	 toolbar
			pos_hint: {"top": 1}
			elevation: 10
			title: "Milk Dairy App"
			left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
			right_action_items:[['account',lambda x: app.redirect_page('members')]]
			md_bg_color: 0,0,100/255,1

		MDNavigationLayout:
			ScreenManager:
				id: screen_manager
				PurchaseSell:
					id:purchasesell
				PriceList:
					id:pricelist
				Setting:
					id:setting
				
			MDNavigationDrawer:
				id: nav_drawer

				ContentNavigationDrawer:
					id: content_drawer
					screen_manager: screen_manager
					nav_drawer: nav_drawer

'''



class LoginScreen(Screen):
	pass
class NavBar(Screen):
	pass
class PurchaseSell(Screen):
	pass
class PriceList(Screen):
	pass
class Setting(Screen):
	pass
class Content(MDBoxLayout):
	pass
class COWList(Screen):
	pass
class BUFFALOList(Screen):
	pass
class Tab(MDFloatLayout, MDTabsBase):
	pass
class ContentNavigationDrawer(MDBoxLayout):
	screen_manager = ObjectProperty()
	nav_drawer = ObjectProperty()
	pass

class TwoLineIconListItem(TwoLineIconListItem):
	icon = StringProperty()
	text_color = ListProperty((0, 0, 0, 1))

class SwipeToDeleteItem(TwoLineAvatarIconListItem):
	text = StringProperty()
	secondary_text = StringProperty()

class DrawerList(ThemableBehavior, MDList):
	def set_color_item(self, instance_item):
		for item in self.children:
			if item.text_color == self.theme_cls.primary_color:
				item.text_color = self.theme_cls.text_color
				break
		instance_item.text_color = self.theme_cls.primary_color

sm = ScreenManager(transition=FadeTransition())
sm.add_widget(LoginScreen(name = 'loginscreen'))
sm.add_widget(NavBar(name = 'application'))
sm.add_widget(PurchaseSell(name = 'purchasesell'))
sm.add_widget(PriceList(name = 'pricelist'))
sm.add_widget(Setting(name = 'setting'))
sm.add_widget(COWList(name = 'cowlist'))
sm.add_widget(BUFFALOList(name = 'buffalo'))

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
		for i in self.rateListJson['cow']:
			self.badgespage.get_screen("application").ids.screen_manager.get_screen("pricelist").ids.screen_manager_tab_price.get_screen("cowlist").ids.tabs_cow.add_widget(Tab(title=f"{i}"))
		for i in self.rateListJson['buffalo']:
			self.badgespage.get_screen("application").ids.screen_manager.get_screen("pricelist").ids.screen_manager_tab_price.get_screen("buffalolist").ids.tabs_buffalo.add_widget(Tab(title=f"{i}"))
		self.load_price_table("cow","7.6")
		self.load_price_table("buffalo","8.5")

	def get_morning(self):
		hour_day = datetime.now().hour
		if (hour_day > 4) and (hour_day <= 12):
			self.badgespage.get_screen("application").ids.screen_manager.get_screen("purchasesell").ids.morning.active = True
		else:
			self.badgespage.get_screen("application").ids.screen_manager.get_screen("purchasesell").ids.evening.active = True

	def on_start(self):
		self.login_check= True
		self.redirect_page("pricelist")
		self.badgespage.get_screen("application").ids.screen_manager.get_screen("purchasesell").ids.field_cnf.disabled = True
		self.badgespage.get_screen("application").ids.screen_manager.get_screen("purchasesell").ids.field_litre.disabled = True
		self.badgespage.get_screen("application").ids.screen_manager.get_screen("purchasesell").ids.purchase_submit.disabled = True
		self.get_morning()
		self.ratelist()
		self.debug()
	
	def flash(self,msgtype, msgtext):
		self.dialog = MDDialog(title = msgtype,text = msgtext,size_hint = (0.7,0.2))
		self.dialog.open()

	def ratelist(self):
		f = open(filename_ratelist,"r")
		fileData = f.read()
		jsonData = json.loads(fileData) if (fileData != "") else {}
		f.close()
		self.rateListJson = jsonData
		return jsonData

	def writeOnfile(self, filename, dataOfJson):
		w= open(filename,"w")
		w.write(dataOfJson)
		w.close()
		return

	def login(self):
		loginEmail = self.badgespage.get_screen('loginscreen').ids.login_email.text
		loginPassword = self.badgespage.get_screen('loginscreen').ids.login_password.text
		if loginEmail.split() == [] and loginPassword.split() ==[]:
			self.flash('Required Credentials',"Please filled out required input.")
		else:
			if loginEmail == "shree" and loginPassword == "123":
				self.login_check=True
				self.redirect_page("purchasesell")
			else:
				self.flash('Incorrect Credentials',"Password not match.")
	
	def accessSetting(self):
		key = self.badgespage.get_screen("application").ids.screen_manager.get_screen('setting').ids.settingpwd.text
		if key.split() == []:
			self.flash('Required Security',"This key is required \nHint: Milk SHREE Dairy")
		else:
			today = datetime.today()
			d2 = today.strftime("%d")
			if key == "shree"+d2:
				self.redirect_page("pricelist")
			else:
				self.flash('Incorrect Security',"Password not match.\nHint: Milk SHREE Dairy")
	
	def pick_op_format(self):
		self.badgespage.get_screen("application").ids.screen_manager.get_screen("purchasesell").ids.field_snf.disabled = False
	
	def assign_snf(self):
		self.badgespage.get_screen("application").ids.screen_manager.get_screen("purchasesell").ids.field_cnf.disabled = False
		try:
			self.output_ext_customer= self.badgespage.get_screen("application").ids.screen_manager.get_screen("purchasesell").ids.search_field.text.split()[0]
		except:
			self.output_ext_customer=None
		

	def assign_cnf(self):
		try:
			self.badgespage.get_screen("application").ids.screen_manager.get_screen("purchasesell").ids.field_litre.disabled = False
			snf = self.badgespage.get_screen("application").ids.screen_manager.get_screen("purchasesell").ids.field_snf.text.split()[0]
			if snf in self.rateListJson[self.output_ext_cow_buffalo]:
				self.output_ext_snf = self.badgespage.get_screen("application").ids.screen_manager.get_screen("purchasesell").ids.field_snf.text.split()[0]
			else:
				self.flash("Error","SNF not found")
		except:
			self.flash("Error","SNF not found")
	
	def assign_litre(self):
		try:
			self.badgespage.get_screen("application").ids.screen_manager.get_screen("purchasesell").ids.purchase_submit.disabled = False
			cnf = self.badgespage.get_screen("application").ids.screen_manager.get_screen("purchasesell").ids.field_cnf.text.split()[0]
			if cnf in self.rateListJson[self.output_ext_cow_buffalo][self.output_ext_snf]:
				self.output_ext_cnf = self.badgespage.get_screen("application").ids.screen_manager.get_screen("purchasesell").ids.field_cnf.text.split()[0]
			else:
				self.flash("Error","CNF not found")
		except:
			self.flash("Error","CNF not found")

	
	def close_popup_cancel_dialog(self, obj):
		self.dataForPrint = None
		self.dialog.dismiss()
		return 1
	
	def top_menu_call(self):
		self.menu.open()

	def calculate_rate(self):
		try:
			rate = self.rateListJson[self.output_ext_cow_buffalo][self.output_ext_snf][self.output_ext_cnf]
			litre = self.badgespage.get_screen("application").ids.screen_manager.get_screen("purchasesell").ids.field_litre.text
			if rate !=0 and rate !="" and litre !="":
				self.badgespage.get_screen("application").ids.screen_manager.get_screen("purchasesell").ids.field_price.text =  str('{0:.3g}'.format(float(rate)*float(litre)))
		except:
			self.flash("Error","Please recheck the value of sssssSNF & CNF")

		
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
			self.generateBill(bill_snf,bill_cnf, bill_customer,bill_cow_b, bill_litre, bill_price, remark, self.output_ext_timing)
		else:
			self.flash("Bill Generate","Something went wrong please try again later.")
		
	# def sendHistory(self,data):
	# 	pass

	def generateBill(self, bill_snf,bill_cnf, bill_customer,bill_cow_b, bill_litre, bill_price, remark, sift):
		today = datetime.today()
		# Textual month, day and year	
		d2 = today.strftime("%d-%m-%Y \n%I:%M %p")
		d3 = today.strftime("%Y%m%d%H%M%S%f")
		recordsOfBill = {"slip": d3, "customer": bill_customer,"date":d2, "sift":sift,"type":bill_cow_b, "snf":bill_snf, "cnf":bill_cnf, "weight":bill_litre, "price":bill_price, "remark":remark}
		# self.sendHistory(json.dumps(recordsOfBill))
		self.printSlip(bill_customer, recordsOfBill, d3)
		

	def on_checkbox_active(self,type ,value, state):
		if type !="timing":
			if state:
				self.output_ext_cow_buffalo= value
		else:
			if state:
				self.output_ext_timing= value

	
	def on_checkbox_pricelist(self, value, state):
		if state:
			self.pricelist_cowb_selection = value
			self.badgespage.get_screen("application").ids.screen_manager.get_screen("pricelist").ids.screen_manager_tab_price.current = "cowlist" if value =="cow" else "buffalolist"
 
		
	def load_price_table(self, typec, snf):
		if typec == "cow":
			self.badgespage.get_screen("application").ids.screen_manager.get_screen("pricelist").ids.screen_manager_tab_price.get_screen("cowlist").ids.pricelist_chart_cow.clear_widgets()
			for i in self.rateListJson[typec][snf]:
				self.badgespage.get_screen("application").ids.screen_manager.get_screen("pricelist").ids.screen_manager_tab_price.get_screen("cowlist").ids.pricelist_chart_cow.add_widget(MDLabel(text=f"{i}", valign="middle"))
				btn = MDTextField(text=f"{self.rateListJson[typec][snf][i]}",helper_text='Required', helper_text_mode= 'on_error',required= True,input_filter= 'float', max_height=200)
				btn.fbind('on_text_validate', self.on_setPriceUpdate, f"{typec}",f"{snf}", f"{i}")
				self.badgespage.get_screen("application").ids.screen_manager.get_screen("pricelist").ids.screen_manager_tab_price.get_screen("cowlist").ids.pricelist_chart_cow.add_widget(btn)
		if typec == "buffalo":
			self.badgespage.get_screen("application").ids.screen_manager.get_screen("pricelist").ids.screen_manager_tab_price.get_screen("buffalolist").ids.pricelist_chart_buffalo.clear_widgets()
			for i in self.rateListJson[typec][snf]:
				self.badgespage.get_screen("application").ids.screen_manager.get_screen("pricelist").ids.screen_manager_tab_price.get_screen("buffalolist").ids.pricelist_chart_buffalo.add_widget(MDLabel(text=f"{i}", valign="middle"))
				btn = MDTextField(text=f"{self.rateListJson[typec][snf][i]}",helper_text='Required', helper_text_mode= 'on_error',required= True,input_filter= 'float', max_height=200)
				btn.fbind('on_text_validate', self.on_setPriceUpdate, f"{typec}",f"{snf}", f"{i}")
				self.badgespage.get_screen("application").ids.screen_manager.get_screen("pricelist").ids.screen_manager_tab_price.get_screen("buffalolist").ids.pricelist_chart_buffalo.add_widget(btn)
	

	def on_tab_switch( self, instance_tabs, instance_tab, instance_tab_label, tab_text ):
		self.load_price_table(self.pricelist_cowb_selection,tab_text)
		# print(self.badgespage.get_screen("application").ids.screen_manager.get_screen("pricelist").ids.screen_manager_tab_price.get_screen("cowlist").ids.pricelist_chart_cow)
 
	
	def on_setPriceUpdate(self, *args, **kwargs):
		try:
			cow_b= args[0]
			snf = args[1]
			cnf = args[2]
			price =args[3].text
			self.rateListJson[cow_b][snf][cnf] = price 
			self.writeOnfile(filename_ratelist, json.dumps(self.rateListJson))
			self.load_price_table(cow_b,snf)
		except:
			self.flash("Update Rate List","Something went wrong please try again.")

	def redirect_page(self, pageName):
		if self.login_check:
			self.badgespage.get_screen('application').manager.current = 'application'
			self.badgespage.get_screen("application").ids.screen_manager.get_screen(pageName).manager.current = pageName
			# self.badgespage.get_screen('application').ids.username_info.text = f"our Customers {self.allUserLen}"
		else:
			self.badgespage.get_screen('loginscreen').manager.current = 'loginscreen'
		
	def printSlip(self,Customer, data, slip):
		self.dataForPrint = data
		aa = Content()
		layout = MDGridLayout(cols = 4, row_force_default = True,row_default_height = 30, spacing=dp(10))
		aa.add_widget(MDLabel(text =data['date'].split("\n" )[0]+data['date'].split("\n" )[1]+" "+data['sift'],valign="bottom",size_hint_y= 0.1))
		layout.add_widget(MDIcon(icon='account'))
		if not(Customer.split() == []):
			layout.add_widget(MDLabel(text =Customer))
		layout.add_widget(MDIcon(icon='cow',halign="right"))
		layout.add_widget(MDLabel(text=data['type'],halign="right"))
		layout.add_widget(MDLabel(text ="SNF"))
		layout.add_widget(MDLabel(text =data['snf']))
		layout.add_widget(MDLabel(text ="FAT",halign="right"))
		layout.add_widget(MDLabel(text =data['cnf'],halign="right"))
		layout.add_widget(MDLabel(text ="Litre"))
		layout.add_widget(MDLabel(text =data['weight']))
		layout.add_widget(MDLabel(text ="Price",halign="right"))
		layout.add_widget(MDLabel(text = str(self.rateListJson[data['type']][data['snf']][data['cnf']]),halign="right"))
		aa.add_widget(MDLabel(text ='	',size_hint_y= 0.5,valign="middle"))
		aa.add_widget(layout)
		aa.add_widget(MDLabel(text ="Total Price: "+ data['price']+"/-",valign="middle",size_hint_y= 0.3))
		aa.add_widget(MDLabel(text =data['remark'],size_hint_y= 0.3, valign="middle"))
		widget = MDLabel(text='[ref=MilkShreeDairy]Print[/ref]', markup=True,valign="bottom",halign="center",size_hint_y= 0.01)
		widget.bind(on_ref_press=self.print_it)
		aa.add_widget(widget)
		self.dialog = MDDialog(
			title="Milk Shree Dairy",
			type="custom",
			content_cls=aa,
			buttons=[
				MDFlatButton(
					text="Cancel", text_color=self.theme_cls.primary_color, on_release = self.close_popup_cancel_dialog
				)
			],
		)
		self.dialog.open()
		self.printData = {"customer": Customer, "time":data['date'].split("\n" )[0]+data['date'].split("\n" )[1]+" "+data['sift'],
	 "slip": slip,"type":data['type'],"snf":data['snf'], "cnf":data['cnf'], "lit":data['weight'],"price":str(self.rateListJson[data['type']][data['snf']][data['cnf']]), "total": data['price'], 'remark':data['remark']}

	def print_it(self,a,b):
		try:
			import webbrowser
			# texthtml = "<table border='0' align='center' style='font-size: small; width : 100%; margin-bottom:10px'> <tr> <th style='border-bottom:2px solid black;padding-bottom: 2px;'>Milk Shree Dairy, Linga,(Kareli)</small> </th> </tr><tr> <th style='padding-top:3px'></th> </tr><tr> <td> &#128100; " + self.printData['customer'] +" </td></tr><tr> <td> &#128338; " + self.printData['time'] +"</td></tr><tr> <th style='border-bottom:1px dotted black'></th> </tr><tr> <td> <table border='0' style='font-size: small; width: 100%;'> <tr> <td style='text-align: left;'># " + self.printData['slip'] +" </td><td style='text-align: right;' style='display: inline-block'>&#128004; " + self.printData['type'] +"</td></tr></table> </td></tr><tr> <td> <table border='0' style='font-size: small; width: 100%;'> <tr> <td> <table border='0' style='font-size: small; width: 100%;'> <tr> <td style='text-align: left; width: 50%;'> SNF: </td><td style='text-align: left; width: 50%;'> " + self.printData['snf'] +"</td></tr></table> </td><td> <table border='0' style='font-size: small; width: 100%;'> <tr> <td style='text-align: right; width: 50%;'> FAT: </td><td style='text-align: right; width: 50%;'> " + self.printData['cnf'] +"</td></tr></table> </td></tr></table> </td></tr><tr> <td> <table border='0' style='font-size: small; width: 100%;'> <tr> <td> <table border='0' style='font-size: small; width: 100%;'> <tr> <td style='text-align: left; width: 50%;'> Lit: </td><td style='text-align: left; width: 50%;'> " + self.printData['lit'] +"</td></tr></table> </td><td> <table border='0' style='font-size: small; width: 100%;'> <tr> <td style='text-align: right; width: 50%;'> Price: </td><td style='text-align: right; width: 50%;'> " + self.printData['price'] +"</td></tr></table> </td></tr></table> </td></tr><tr> <td style='border-bottom:1px dotted black'></td></tr><tr> <td style='text-align: center;'>Total Price	" +self.printData['total'] +":</td></tr><tr> <td style='text-align: center;'>"+ self.printData['remark']+ "</td></tr></table>"
			if not(Customer.split() == []):
				customer = "<LEFT>C: "+ self.printData['customer'] +"<BR>"
			texthtml = "<CENTER><BOLD>Milk Shree Dairy<NORMAL><BR><CENTER><LINE>"+customer+"<LEFT>T: "+self.printData['time']+"<BR><LEFT>#: "+self.printData['slip']+"		<RIGHT>C/B: "+self.printData['type']+"<BR><LEFT>SNF: "+self.printData['snf']+"			  <RIGHT>FAT: "+self.printData['cnf']+"<BR><LEFT>Lit: "+self.printData['lit']+"			  <RIGHT>Price: "+self.printData['price']+"<BR><CENTER><LINE><CENTER><BOLD>Total Price: "+self.printData['total']+"<BR><NORMAL>"+self.printData['remark']
			webbrowser.open("https://rajp7jowa.github.io/krashishakti/milkshree.html?intent://"+texthtml+"#Intent;scheme=quickprinter;package=pe.diegoveloper.printerserverapp;end;")			
		except:
			self.flash("Print Slip","Something went wrong to your mobile browser.")
if __name__ == '__main__':
	MilkApp().run()