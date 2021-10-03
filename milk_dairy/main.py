from kivy.lang import Builder
from kivy.properties import StringProperty, ListProperty,ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.metrics import dp
from kivymd.app import MDApp
from kivymd.theming import ThemableBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import OneLineListItem,TwoLineIconListItem, MDList
from kivymd.uix.button import MDFlatButton,MDRectangleFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.behaviors.toggle_behavior import MDToggleButton
from kivymd.uix.card import MDCardSwipe
from kivymd.uix.label import MDLabel,MDIcon
from kivymd.uix.textfield import MDTextField
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.gridlayout import MDGridLayout
import copy
from datetime import datetime
import json
import os

filename_members = "./assets/members.txt"
filename_ratelist = "./assets/ratelist.txt"
filename_history = "./assets/history.txt"

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
		do_scroll_x: False
		DrawerList:
			id:md_list
			OneLineIconListItem:
				size_hint: (1, 0.04)
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
		text:"admin"
		size_hint : (0.95,0.1)
		hint_text: 'Security Key'
		helper_text:'Required'
		helper_text_mode:  'on_error'
		icon_right: 'account-key'
		icon_right_color: app.theme_cls.primary_color
		required: True
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
	height: content.height
	
    MDCardSwipeLayerBox:
        padding: "8dp"

        MDIconButton:
            icon: "trash-can"
            pos_hint: {"center_y": .5}
            on_press: app.remove_customer(root.secondary_text)
			
	MDCardSwipeFrontBox:

		TwoLineListItem:
			id: content
			text: root.text
			secondary_text: root.secondary_text
			_no_ripple_effect: True
			on_release: app.bill_history(root.secondary_text)
		

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
		pos_hint: {'center_y':0.65,'center_x':0.5}
		cols: 2
		MDBoxLayout:
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
				on_focus: 
					app.assign_snf()
					if self.focus: app.menu_snf.open()


	MDGridLayout:
		size_hint : (1,0.1)
		pos_hint: {'center_y':0.53,'center_x':0.5}
		cols: 2
		MDBoxLayout:
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
					text: 'buffalo'
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
				on_focus:
					app.assign_cnf()
					if self.focus: app.menu_cnf.open()
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

	ScrollView:
		pos_hint: {'center_y':0.70,'center_x':0.5}
		size_hint: (0.99,0.07)
		orientation: "vertical"
		do_scroll_y: False

		MDBoxLayout:
			adaptive_size: True
			id: tabs_price
		
	MDCard:
		padding: "10dp"
		size_hint: (0.99,0.67)
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
				spacing: dp(30),dp(10)
				cols: 2
				size_hint_y: None
				size_hint_x: 1
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
	spacing: "7dp"
	padding: "7dp"
	size_hint_y: None
	height: "150dp"

<MyToggleButton>
	on_press:app.on_loadPrice_list(self.text)

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
				SignupScreen:
				Members:
					id:members
				PurchaseSell:
					id:purchasesell
				PriceList:
					id:pricelist
				HistoryPage:
					id:history
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
class HistoryPage(Screen):
	pass
class Setting(Screen):
	pass
class Content(MDBoxLayout):
	pass
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

sm = ScreenManager(transition=FadeTransition())
sm.add_widget(LoginScreen(name = 'loginscreen'))
sm.add_widget(SignupScreen(name = 'signupscreen'))
sm.add_widget(NavBar(name = 'application'))
sm.add_widget(Members(name = 'members'))
sm.add_widget(PurchaseSell(name = 'purchasesell'))
sm.add_widget(PriceList(name = 'pricelist'))
sm.add_widget(HistoryPage(name = 'historypage'))
sm.add_widget(Setting(name = 'setting'))


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
		pass
		
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
	
	def allMembersList(self):
		self.badgespage.get_screen("application").ids.members.ids.membersList.clear_widgets()
		for key in self.allUser:
			if key !="admin":
				self.badgespage.get_screen("application").ids.members.ids.membersList.add_widget(
					SwipeToDeleteItem(text=f"{self.allUser[key]['UserName']}",secondary_text=f"{key}")
				)

	def flash(self,msgtype, msgtext):
		cancel_btn_username_dialogue = MDFlatButton(text = 'Retry',on_release = self.close_popup_cancel_dialog)
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
		self.forDelete = mobile
		self.dialog = MDDialog(
		title="Delete member ?",
		text="are you want to delete member.user: \n"+self.allUser[mobile]['UserName'],
			buttons=[
				MDFlatButton(
					text="Cancel", text_color=self.theme_cls.primary_color, on_release = self.close_popup_cancel_dialog
				),
				MDFlatButton(
					text="Delete", text_color=self.theme_cls.primary_color, on_release = self.remove_customer_final
				),
			],
		)
		self.dialog.open()

	def bill_history(self, mobile):
		self.badgespage.get_screen("application").ids.screen_manager.get_screen("historypage").ids.historypageCustomer.title = mobile
		self.badgespage.get_screen("application").ids.screen_manager.get_screen("historypage").ids.historypageCustomer1.text = self.allUser[mobile]['UserName']
		self.dataTablePlot(mobile)
	
	def dataTablePlot(self, mobile):
		try:
			self.temp_user_show = mobile
			self.get_history()
			self.badgespage.get_screen("application").ids.screen_manager.get_screen("historypage").ids.historypageDataTable.clear_widgets()
			data= []
			historical_data = copy.deepcopy(self.history[mobile])
			for f in copy.deepcopy(self.history[mobile]):
				historical_data[f]["key"] = "[size=0]"+f+"[/size]"
				data.append(tuple(historical_data[f].values()))
			data_tables = MDDataTable(
				column_data=[
					("Date.", dp(20)),
					("Sift", dp(15)),
					("Type", dp(13)),
					("SNF", dp(10)),
					("FAT", dp(10)),
					("Litre", dp(10)),
					("Price", dp(13)),
					("Remark", dp(40)),
					("", dp(0)),
				],
				row_data=data
			)
			data_tables.bind(on_row_press=self.on_row_press)
			self.badgespage.get_screen("application").ids.screen_manager.get_screen("historypage").ids.historypageDataTable.add_widget(data_tables)
			self.redirect_page("historypage")
		except:
			self.flash("Fetch bill history","records not found.")

	def on_row_press(self, instance_table, instance_row):
		filtered = instance_row.table.recycle_data[instance_row.table.recycle_data[instance_row.index]["range"][1]]['text'].split("[size=0]")[1].split("[/size]")[0]
		generateBill = self.history[self.temp_user_show][filtered]
		self.printSlip(self.temp_user_show, generateBill, filtered)

	
	def remove_customer_final(self, obj):
		jsonData = self.alluser()
		del jsonData[self.forDelete]
		self.allUserLen = len(jsonData)
		self.allUser = jsonData
		self.allMembersList()
		self.writeOnfile(filename_members, json.dumps(jsonData))
		self.dialog.dismiss()
		self.forDelete = None
		

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
	
	def accessSetting(self):
		key = self.badgespage.get_screen("application").ids.screen_manager.get_screen('setting').ids.settingpwd.text
		if key.split() == []:
			self.flash('Required Credentials',"This key is required \n Hint: Milk SHREE Dairy")
		else:
			today = datetime.today()
			d2 = today.strftime("%d")
			if key == "shree"+d2:
				self.redirect_page("pricelist")
			else:
				self.flash('Incorrect Credentials',"Password not match.")
	
	def gen_op_list(self, text="", search=False):
		listOfMenu = []
		def add_icon_item(format, secondtext):
			listOfMenu.append(
				{
					"viewclass": "CustomOneLineIconListItem",
					"text": "[b] "+secondtext+" [/b]"+ format
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
		# self.menu_snf.bind(on_release=self.menu_callback)

	# def menu_callback(self, instance_menu, instance_menu_item):
	# 	print(instance_menu, instance_menu_item)


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
	

	def close_popup_cancel_dialog(self, obj):
		self.forDelete = None
		self.dataForPrint = None
		self.dialog.dismiss()
	
	def top_menu_call(self):
		self.menu.open()

	def pick_op_format(self, format):
		self.badgespage.get_screen("application").ids.screen_manager.get_screen("purchasesell").ids.field_snf.disabled = False
		self.output_ext_customer= format.split("[/b]")[1]
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
			self.badgespage.get_screen("application").ids.screen_manager.get_screen("purchasesell").ids.field_price.text =  str('{0:.3g}'.format(float(rate)*float(litre)))
			
		
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
			flash("Bill Generate","Something went wrong please try again later.")
		
	def generateBill(self, bill_snf,bill_cnf, bill_customer,bill_cow_b, bill_litre, bill_price, remark, sift):
		today = datetime.today()
		# Textual month, day and year	
		d2 = today.strftime("%d-%m-%Y \n%I:%M %p")
		d3 = today.strftime("%Y%m%d%H%M%S")
		self.get_history()
		recordsOfBill = {"date":d2, "sift":sift,"type":bill_cow_b, "snf":bill_snf, "cnf":bill_cnf, "weight":bill_litre, "price":bill_price, "remark":remark}
		if bill_customer in self.history:
			self.history[bill_customer][d3] = recordsOfBill
		else:
			self.history[bill_customer] = {d3:recordsOfBill}
		self.writeOnfile(filename_history, json.dumps(self.history))
		self.printSlip(bill_customer, recordsOfBill, d3)
		

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
			self.badgespage.get_screen("application").ids.screen_manager.get_screen("pricelist").ids.tabs_price.add_widget(MyToggleButton(text=f"{i}", group="tab_button"))

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
			btn = MDTextField(text=f"{self.rateListJson[self.pricelist_cowb_selection][self.pricelist_snf_selection][i]}", halign="center",helper_text='Required', helper_text_mode= 'on_error',required= True,input_filter= 'float', max_height=200)
			btn.fbind('on_text_validate', self.on_setPriceUpdate, f"{self.pricelist_cowb_selection}",f"{self.pricelist_snf_selection}", f"{i}")
			self.badgespage.get_screen("application").ids.screen_manager.get_screen("pricelist").ids.pricelist_chart.add_widget(btn)
 
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
		
	def printSlip(self,Customer, data, slip):
		self.dataForPrint = data
		aa = Content()
		layout = MDGridLayout(cols = 4, row_force_default = True,row_default_height = 30, spacing=dp(10))
		aa.add_widget(MDLabel(text =data['date'].split("\n" )[0]+data['date'].split("\n" )[1]+" "+data['sift'],valign="bottom",size_hint_y= 0.1))
		layout.add_widget(MDIcon(icon='account'))
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
		aa.add_widget(layout)
		aa.add_widget(MDLabel(text ="Total Price: "+ data['price']+"/-",valign="bottom",size_hint_y= 0.5	))
		aa.add_widget(MDLabel(text =data['remark'],size_hint_y= 0.01, valign="bottom"))
		widget = MDLabel(text='[ref=MilkShreeDairy]Print[/ref]', markup=True,valign="bottom",halign="center")
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
		import webbrowser
		texthtml = "%3Ctable%20border%3D%220%22%20align%3D%22center%22%20style%3D%22font-size%3A%20small%3B%20width%20%3A%20100%25%3B%20margin-bottom%3A10px%22%3E%20%3Ctr%3E%20%3Cth%20style%3D%27border-bottom%3A2px%20solid%20black%3Bpadding-bottom%3A%202px%3B%27%3EMilk%20Shree%20Dairy%2C%20%3Csmall%3ELinga%2C(Kareli)%3C%2Fsmall%3E%20%3C%2Fth%3E%20%3C%2Ftr%3E%3Ctr%3E%20%3Cth%20style%3D%27padding-top%3A3px%27%3E%3C%2Fth%3E%20%3C%2Ftr%3E%3Ctr%3E%20%3Ctd%3E%20%26%23128100%3B%20"+self.printData['customer']+"%20%3C%2Ftd%3E%3C%2Ftr%3E%3Ctr%3E%20%3Ctd%3E%20%26%23128338%3B%20"+self.printData['time']+"%3C%2Ftd%3E%3C%2Ftr%3E%3Ctr%3E%20%3Cth%20style%3D%27border-bottom%3A1px%20dotted%20black%27%3E%3C%2Fth%3E%20%3C%2Ftr%3E%3Ctr%3E%20%3Ctd%3E%20%3Ctable%20border%3D%220%22%20style%3D%22font-size%3A%20small%3B%20width%3A%20100%25%3B%22%3E%20%3Ctr%3E%20%3Ctd%20style%3D%22text-align%3A%20left%3B%22%3E%23%20"+self.printData['slip']+"%20%3C%2Ftd%3E%3Ctd%20style%3D%22text-align%3A%20right%3B%22%20style%3D%27display%3A%20inline-block%27%3E%26%23128004%3B%20"+self.printData['type']+"%3C%2Ftd%3E%3C%2Ftr%3E%3C%2Ftable%3E%20%3C%2Ftd%3E%3C%2Ftr%3E%3Ctr%3E%20%3Ctd%3E%20%3Ctable%20border%3D%220%22%20style%3D%22font-size%3A%20small%3B%20width%3A%20100%25%3B%22%3E%20%3Ctr%3E%20%3Ctd%3E%20%3Ctable%20border%3D%220%22%20style%3D%22font-size%3A%20small%3B%20width%3A%20100%25%3B%22%3E%20%3Ctr%3E%20%3Ctd%20style%3D%22text-align%3A%20left%3B%20width%3A%2050%25%3B%22%3E%20SNF%3A%20%3C%2Ftd%3E%3Ctd%20style%3D%22text-align%3A%20left%3B%20width%3A%2050%25%3B%22%3E%20"+self.printData['snf']+"%3C%2Ftd%3E%3C%2Ftr%3E%3C%2Ftable%3E%20%3C%2Ftd%3E%3Ctd%3E%20%3Ctable%20border%3D%220%22%20style%3D%22font-size%3A%20small%3B%20width%3A%20100%25%3B%22%3E%20%3Ctr%3E%20%3Ctd%20style%3D%22text-align%3A%20right%3B%20width%3A%2050%25%3B%22%3E%20FAT%3A%20%3C%2Ftd%3E%3Ctd%20style%3D%22text-align%3A%20right%3B%20width%3A%2050%25%3B%22%3E%20"+self.printData['cnf']+"%3C%2Ftd%3E%3C%2Ftr%3E%3C%2Ftable%3E%20%3C%2Ftd%3E%3C%2Ftr%3E%3C%2Ftable%3E%20%3C%2Ftd%3E%3C%2Ftr%3E%3Ctr%3E%20%3Ctd%3E%20%3Ctable%20border%3D%220%22%20style%3D%22font-size%3A%20small%3B%20width%3A%20100%25%3B%22%3E%20%3Ctr%3E%20%3Ctd%3E%20%3Ctable%20border%3D%220%22%20style%3D%22font-size%3A%20small%3B%20width%3A%20100%25%3B%22%3E%20%3Ctr%3E%20%3Ctd%20style%3D%22text-align%3A%20left%3B%20width%3A%2050%25%3B%22%3E%20Lit%3A%20%3C%2Ftd%3E%3Ctd%20style%3D%22text-align%3A%20left%3B%20width%3A%2050%25%3B%22%3E%20"+self.printData['lit']+"%3C%2Ftd%3E%3C%2Ftr%3E%3C%2Ftable%3E%20%3C%2Ftd%3E%3Ctd%3E%20%3Ctable%20border%3D%220%22%20style%3D%22font-size%3A%20small%3B%20width%3A%20100%25%3B%22%3E%20%3Ctr%3E%20%3Ctd%20style%3D%22text-align%3A%20right%3B%20width%3A%2050%25%3B%22%3E%20Price%3A%20%3C%2Ftd%3E%3Ctd%20style%3D%22text-align%3A%20right%3B%20width%3A%2050%25%3B%22%3E%20"+self.printData['price']+"%3C%2Ftd%3E%3C%2Ftr%3E%3C%2Ftable%3E%20%3C%2Ftd%3E%3C%2Ftr%3E%3C%2Ftable%3E%20%3C%2Ftd%3E%3C%2Ftr%3E%3Ctr%3E%20%3Ctd%20style%3D%27border-bottom%3A1px%20dotted%20black%27%3E%3C%2Ftd%3E%3C%2Ftr%3E%3Ctr%3E%20%3Ctd%20style%3D%27text-align%3A%20center%3B%27%3ETotal%20Price%20%20%20%20"+self.printData['total']+"%3A%3C%2Ftd%3E%3C%2Ftr%3E%3Ctr%3E%20%3Ctd%20style%3D%27text-align%3A%20center%3B%27%3E"+self.printData['remark']+"%3C%2Ftd%3E%3C%2Ftr%3E%3C%2Ftable%3E";
		webbrowser.open("https://rajp7jowa.github.io/krashishakti/milkshree.html?intent://"+texthtml+"#Intent;scheme=quickprinter;package=pe.diegoveloper.printerserverapp;end;")			
		print(os.getcwd())
		# MDLabel:
		# 	id: need_help_link
		# 	font_size: 20
		# 	markup: True
		# 	text: 'Need help [ref=some]someweblink[/ref]'
		# 	on_ref_press:
		# 		import webbrowser
		# 		webbrowser.open('http://google.com')			


if __name__ == '__main__':
	MilkApp().run()