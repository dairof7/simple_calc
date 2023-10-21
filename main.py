import flet as ft
from flet import (
    Column,
    Container,
    ElevatedButton,
    Row,
    Text,
    UserControl,
    border_radius,
    colors,
)


class num_btn(ft.UserControl):
    def __init__(self, value, click_fn):
        super().__init__()
        self.value = value
        self.fn = click_fn
    def build(self):
        def btn_clicked(e):
            self.value = e.control.data
            self.update()
            print(self.value)
        btn = ElevatedButton(
            text=str(self.value),
            bgcolor='#04293A',
            color=colors.WHITE,
            expand=1,
            on_click=self.fn,
            data=self.value,
        )
        return btn


class CalculatorApp(UserControl):
    def btn_clicked(self, e):
        value = e.control.data
        print(f'value {value}')
        print(f'self.to_operate {self.to_operate}')
            
        if value in ['1','2','3','4','5','6','7','8','9','0'] and self.to_operate == False:
            if self.result.value in ['0', 'Error Div 0'] :
                self.result.value = value
            else:
                self.result.value += value
        elif value in ['1','2','3','4','5','6','7','8','9','0'] and self.to_operate == True:
            self.result.value = value
        
        if value in ['+','-','*','/'] and value != 'Error Div 0':
            if self.to_operate == False:
                self.to_operate = True
            self.operator = value
            self.num1 = self.result.value
            
        if value == '=' and self.to_operate == True:
            self.operate()
        self.update()
    def reset(self):
        self.result.value = '0'
        self.num1 = '0'
        self.operator = None
        self.to_operate = False
        self.update()
    def operate(self):
        num1 = float(self.num1)
        num2 = float(self.result.value)
        if self.operator == '+':
            res = num1 + num2
        elif self.operator == '-':
            res = num1 - num2
        elif self.operator == '*':
            res = num1 * num2
        elif self.operator == '/':
            if num2 == 0:
                res = 'Error Div 0'
            else:
                res = num1 / num2
        else:
            res = None
        if type(res) != str:
            res = str(res)
            if res[-2:] == '.0':
                res = int(res[:-2])
            print(res)
        self.result.value = res
        self.to_operate = False
    def build(self): 
        self.to_operate = False
        add_btn = ElevatedButton(
            text="+",
            bgcolor='#ECB365',
            color=colors.WHITE,
            expand=1,
            on_click=self.btn_clicked,
            data="+",
        )
        sub_btn = ElevatedButton(
            text="-",
            bgcolor='#ECB365',
            color=colors.WHITE,
            expand=1,
            on_click=self.btn_clicked,
            data="-",
        )
        div_btn = ElevatedButton(
            text="/",
            bgcolor='#ECB365',
            color=colors.WHITE,
            # expand=1,
            on_click=self.btn_clicked,
            data="/",
        )
        reset_btn = ElevatedButton(
            text="AC",
            bgcolor='#064663',
            color='#ECB365',
            expand=1,
            on_click=self.btn_clicked,
            data="reset",
        )
        mul_btn = ElevatedButton(
            text="*",
            bgcolor='#ECB365',
            color=colors.WHITE,
            expand=1,
            on_click=self.btn_clicked,
            data="*",
        )
        exe_btn = ElevatedButton(
            text="=",
            bgcolor='#ECB365',
            color=colors.WHITE,
            expand=1,
            on_click=self.btn_clicked,
            data="=",
        )
        dot_btn = ElevatedButton(
            text=".",
            bgcolor='#ECB365',
            color=colors.WHITE,
            # expand=1,
            on_click=self.btn_clicked,
            data=".",
        )
        
        self.result = Text(value="0", color=colors.WHITE, size=20, expand=1, text_align='end')
        return Container(
            width=300,
            bgcolor='#041C32',
            border_radius=border_radius.all(20),
            padding=20,
            content=Column(
                controls=[
                    Row(controls=[self.result], alignment="end"),
                    Row(controls=[reset_btn, div_btn], alignment="end"),
                    Row(controls=[num_btn('7',self.btn_clicked), num_btn('8',self.btn_clicked), num_btn('9',self.btn_clicked), mul_btn]),
                    Row(controls=[num_btn('4',self.btn_clicked), num_btn('5',self.btn_clicked), num_btn('6',self.btn_clicked), sub_btn]),
                    Row(controls=[num_btn('1',self.btn_clicked), num_btn('2',self.btn_clicked), num_btn('3',self.btn_clicked), add_btn]),
                    Row(controls=[num_btn('0',self.btn_clicked), dot_btn, exe_btn]),
                ]
            )
        )

def main(page):
    page.title = "Simple-Calc App"
    calc = CalculatorApp()
    page.add(
        calc
    )

# ft.app(target=main, view = ft.AppView.WEB_BROWSER)
ft.app(port=8080, target=main, view = ft.AppView.WEB_BROWSER)