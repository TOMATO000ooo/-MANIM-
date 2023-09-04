from manim import *
class ercidingdian01(Scene):
    def construct(self):
        text1 = Text("我们都知道二次函数可以写成:", font="STSong")
        text2 = MathTex("f(x)=ax^{2} +bx+c(a\\ne 0)").next_to(text1,DOWN).set_color_by_gradient(RED,YELLOW)
        T101 = VGroup(text1,text2)
        self.play(Write(T101))
        self.play(FadeOut(T101))
        text3 = Text("如果二次函数的系数a和c固定,只动b", font="STSong").shift(UP*1)
        text4 = Text("其顶点的轨迹会是什么?", font="STSong").next_to(text3,DOWN)
        text401 = Text("Made by TOMATOooo").next_to(text4,DOWN,buff=2)
        text401[6:15].set_color_by_gradient(RED,YELLOW)
        juxing = Rectangle(height=0.9, width=7.0).move_to(text401).set_color(TEAL)
        T10 = VGroup(text401,juxing)
        self.play(Write(text3))
        self.play(Write(text4))
        self.wait()
        self.play(FadeIn(T10))
        self.wait(1.5)
        self.play(LaggedStart(FadeOut(text3),FadeOut(text4),FadeOut(T10)))
        self.wait()       
        text7 = Text("我们直接看最简单的情况", font="STSong")
        text8 = MathTex("a=1;c=0").next_to(text7,DOWN)
        self.play(Write(text7))
        self.play(Write(text8))
        self.wait(1.5)
        self.play(LaggedStart(FadeOut(text7),FadeOut(text8)))
        self.wait()  

        zuobiaozhou1 = (
            Axes(
                x_range=[-3,3.1,1],
                x_length=2,
                y_range=[-9,9.1,1],
                y_length=6
            ).add_coordinates().set_color(GREEN).shift(UP*0.3)           
        )
        text3 = Text("我们不妨拉伸一下真实比例的x轴", font="STSong").next_to(zuobiaozhou1,DOWN,buff=0.4)
        hanshu1 = zuobiaozhou1.plot(lambda x : x**2,x_range=[-3,3],color=BLUE)
        hanshu1_lab = (
            MathTex("h(x)={x}^{2}").scale(0.8).next_to(hanshu1,UR,buff=0.1).set_color(BLUE)
        )
        T1 = VGroup(hanshu1,hanshu1_lab)
        T3 = VGroup(T1,zuobiaozhou1)

        
        zuobiaozhou2 = (
            Axes(
                x_range=[-6,6,1],
                x_length=6,
                y_range=[-3.1,9.1,3],
                y_length=6
            ).shift(UP*0.3)          
        )
        hanshu2 = zuobiaozhou2.plot(lambda x : x**2,x_range=[-3,3],color=BLUE)
        hanshu2_lab = (
            MathTex("h(x)={x}^{2}").scale(0.8).next_to(hanshu2,UR,buff=0.1).set_color(BLUE)
        )
        T2 = VGroup(hanshu2,hanshu2_lab)
        T4 = VGroup(T2,zuobiaozhou2)
        
   
        self.play(Write(T3))
        self.play(Write(text3))
        self.play(FadeOut(text3))
        self.play(Transform(T3,T4))



        b1 = ValueTracker(-3)
        dongtaihanshu = always_redraw(lambda:
        zuobiaozhou2.plot(lambda x : x**2+b1.get_value()*x,color=YELLOW))
        dongtaihanshu1_lab = MathTex("f(x)={x}^{2}").scale(0.8).shift(UP*2,RIGHT*3.3).set_color(YELLOW)
        dongtaihanshu2_lab = always_redraw(lambda:DecimalNumber(num_decimal_places=1,include_sign=True).set_value(b1.get_value())).next_to(dongtaihanshu1_lab,RIGHT,buff=0)
        dongtaihanshu2_lab.add_updater(
            lambda mobject:mobject.next_to(dongtaihanshu1_lab,RIGHT,buff=0).set_color(YELLOW).scale(0.8)
        )
        dongtaihanshu3_lab = MathTex("{x}").scale(0.8).next_to(dongtaihanshu2_lab,RIGHT,buff=0).set_color(YELLOW)
        


        T5 = VGroup(dongtaihanshu,dongtaihanshu1_lab,dongtaihanshu2_lab,dongtaihanshu3_lab)

        text5 = Text("这次我加上顶点", font="STSong").next_to(zuobiaozhou2,DOWN,buff=0.4)

        dingdian = always_redraw(lambda:Dot().set_color(PINK).move_to(
            zuobiaozhou2.c2p(b1.get_value()*(-1/2),dongtaihanshu.underlying_function(b1.get_value()*(-1/2)))))
        
        T6 = VGroup(T5,dingdian)



        self.play(Write(T5))
        self.play(b1.animate.set_value(3),run_time=6,rate_func=smooth)
        self.play(FadeOut(T5))
        self.play(Write(text5))
        self.play(FadeOut(text5))
        self.play(Write(T6))
        b1 = ValueTracker(-3)
        self.play(b1.animate.set_value(3),run_time=6,rate_func=smooth)
        self.wait()

        text5 = Text("有看出来什么端倪吗?", font="STSong").next_to(zuobiaozhou2,DOWN,buff=0.4)
        text6 = Text("没事,我再加上一条曲线", font="STSong").next_to(zuobiaozhou2,DOWN,buff=0.4)
        self.play(Write(text5))
        self.wait()
        self.play(Transform(text5,text6))
        self.wait()
        self.play(FadeOut(text5))

        hanshu3 = zuobiaozhou2.plot(lambda x : -x**2,x_range=[-3,3],color=TEAL)
        self.play(Write(hanshu3))
        b1 = ValueTracker(3)
        self.play(b1.animate.set_value(-3),run_time=6,rate_func=smooth)
        self.wait()
        text6 = Text("揭晓答案", font="STSong").next_to(zuobiaozhou2,DOWN,buff=0.4)
        hanshu3_lab = (
            MathTex("h(x)=-{x}^{2}").scale(0.8).next_to(hanshu3,RIGHT,buff=0.1).set_color(TEAL)
        )
        self.play(Write(text6))
        self.play(Write(hanshu3_lab))
        self.wait()





class ercidingdian02(Scene):
    def construct(self):
        text7 = Text("再来看看更一般的情况", font="STSong")
        self.play(Write(text7))
        self.play(FadeOut(text7))
        zuobiaozhou3 = (
            Axes(
                x_range=[-6,6,1],
                x_length=6,
                y_range=[-3.1,9.1,3],
                y_length=6
            )         
        )
        self.play(Write(zuobiaozhou3))
        hanshu3 = zuobiaozhou3.plot(lambda x : x**2-2*x+3,x_range=[-3,6],color=BLUE)
        hanshu3_lab = (
            MathTex("h(x)={ax}^{2}+{bx}+{c}").scale(0.8).next_to(hanshu3,DR,buff=0.1).set_color(BLUE).shift(UP*4)
        )
        T7 = VGroup(hanshu3,hanshu3_lab)
        self.play(Write(T7))
        b1 = ValueTracker(-3)
        dongtaihanshu = always_redraw(lambda:
        zuobiaozhou3.plot(lambda x : x**2+b1.get_value()*x+3,color=YELLOW))
        dingdian = always_redraw(lambda:Dot().set_color(PINK).move_to(
            zuobiaozhou3.c2p(b1.get_value()*(-1/2),dongtaihanshu.underlying_function(b1.get_value()*(-1/2)))))
        T8 = VGroup(dongtaihanshu,dingdian)
        self.play(Write(T8))
        self.play(b1.animate.set_value(2.99),run_time=6,rate_func=smooth)
        self.wait()
        hanshu4 = zuobiaozhou3.plot(lambda x : -x**2+3,x_range=[-3,6],color=TEAL)
        self.play(Write(hanshu4))
        b1 = ValueTracker(3)
        self.play(b1.animate.set_value(-3),run_time=6,rate_func=smooth)
        self.wait()





class ercidingdian03(Scene):
    def construct(self):
        text8 = Text("接下来是推导", font="STSong")
        self.play(Write(text8))
        self.wait(0.5)
        self.play(FadeOut(text8))
        text9 = Text("我们都知道二次函数顶点的坐标可以写成:", font="STSong").shift(UP*1)
        text10 = MathTex("(-\\frac{b}{2a},\\frac{4ac-b^{2} }{4a}  )").next_to(text9,DOWN).set_color_by_gradient(RED,YELLOW)
        self.play(Write(text9))
        self.play(Write(text10))
        self.play(FadeOut(text9))
        self.play(text10.animate.to_edge(UP))
        text11 = Text("先把x的坐标整体平方", font="STSong").next_to(text10,DOWN)
        text12 = MathTex("(-\\frac{b}{2a} )^{2}=\\frac{b^{2} }{4a^{2} }\\Rightarrow x^{2} ").next_to(text11,DOWN)
        self.play(Write(text11))
        self.wait()
        self.play(Write(text12))
        self.wait()
        text13 = Text("为了凑分母我们再乘上a", font="STSong").next_to(text12,DOWN)
        text14 = MathTex("\\frac{b^{2} }{4a^{2} }\\times a=\\frac{b^{2} }{4a}\\Rightarrow ax^{2} ").next_to(text13,DOWN)
        self.play(Write(text13))
        self.wait()
        self.play(Write(text14))
        self.wait()
        text15 = MathTex("\\frac{b^{2} }{4a}=ax^{2} ",color=YELLOW).next_to(text10,DOWN)
        T9 = VGroup(text11,text12,text13,text14)
        self.play(Transform(T9,text15))
        self.wait(0.5)
        
        self.wait()
        text16 = Text("我们注意到分母可以写成:", font="STSong").next_to(T9,DOWN)
        self.play(Write(text16))
        text17 = MathTex("y=\\frac{4ac-b^{2} }{4a}=c-\\frac{b^{2} }{4a}").next_to(text16,DOWN)
        self.play(Write(text17))
        self.wait()
        text18 = MathTex("y=c-ax^{2} ").next_to(text17,DOWN).shift(RIGHT*1.35).set_color(TEAL)
        self.play(Write(text18))
        self.wait()
        juxing = Rectangle( height=0.9, width=3.0).move_to(text18).set_color(RED)
        self.play(Write(juxing))
        text19 = Text("这就是轨迹方程了哈", font="STSong").next_to(juxing,DOWN).set_color(TEAL)
        self.play(Write(text19))
        self.wait()


class ercidingdian04(Scene):
    def construct(self):
        text20 = Text("综上,我们可以得出结论:", font="STSong").shift(UP*1.5)
        text21 = Text("对于任意的二次函数", font="STSong").next_to(text20,DOWN).shift(LEFT*3)
        text22 = MathTex("h(x)={ax}^{2}+{bx}+{c}").next_to(text21,RIGHT).set_color(YELLOW)
        T1 = VGroup(text21,text22)
        self.play(Write(text20))
        self.play(Write(T1))
        text23 = Text("如果该二次函数的系数a和c固定,只动b", font="STSong").next_to(T1,DOWN)
        text24 = Text("其顶点的轨迹为:", font="STSong").next_to(text23,DOWN).shift(LEFT*2)
        text25 = MathTex("f(x)=-{ax}^{2}+{c}").next_to(text24,RIGHT).set_color(GREEN)
        T2 = VGroup(text24,text25)
        text26 = Text("接下来展示一点直观的东西......", font="STSong").next_to(T2,DOWN)
        self.play(Write(text23))
        self.play(Write(T2))
        self.wait()
        self.play(Write(text26))
        self.wait()





class ercidingdian05(Scene):
    def construct(self):
        zuobiaozhou3 = (
            Axes(
                x_range=[-6,6,1],
                x_length=6,
                y_range=[-3.1,9.1,3],
                y_length=6
            )         
        )
        self.play(Write(zuobiaozhou3))
        hanshu3 = zuobiaozhou3.plot(lambda x : x**2-2*x+3,x_range=[-3,6],color=BLUE)
        hanshu3_lab = (
            MathTex("h(x)={ax}^{2}+{bx}+{c}").scale(0.8).next_to(hanshu3,DR,buff=0.1).set_color(BLUE).shift(UP*4)
        )
        T7 = VGroup(hanshu3,hanshu3_lab)
        hanshu4 = zuobiaozhou3.plot(lambda x : x**2+3,x_range=[-3,6],color=YELLOW)
        hanshu4_lab = (
            MathTex("h(x)={ax}^{2}+{c}").scale(0.8).next_to(hanshu4,DR,buff=0.1).set_color(YELLOW).shift(UP*3)
        )
        T8 = VGroup(hanshu4,hanshu4_lab)
        self.play(Write(T7))
        self.wait()
        self.play(Transform(T7,T8),run_time=1)
        self.wait()
        self.play(
            Rotate(
                hanshu4,
                angle=PI,
                about_point=ORIGIN,
                rate_func=smooth,
            )
        )
        hanshu9 = zuobiaozhou3.plot(lambda x : -x**2+3,x_range=[-3,6],color=TEAL)
        self.play(Write(hanshu9))
        self.wait(0.5)
        text1 = MathTex("f(x)=-{ax}^{2}+{c}").move_to(hanshu4_lab,DOWN).scale(0.8).set_color(TEAL).shift(DOWN*6)
        self.play(Write(text1))
        self.wait(0.5)
        b1 = ValueTracker(0)
        dongtaihanshu = always_redraw(lambda:
        zuobiaozhou3.plot(lambda x : x**2+b1.get_value()*x+3,color=YELLOW))
        dingdian = always_redraw(lambda:Dot().set_color(PINK).move_to(
            zuobiaozhou3.c2p(b1.get_value()*(-1/2),dongtaihanshu.underlying_function(b1.get_value()*(-1/2)))))
        T8 = VGroup(dongtaihanshu,dingdian)
        self.play(Write(T8))
        self.play(b1.animate.set_value(3),run_time=6,rate_func=smooth)
        self.wait()
        b1 = ValueTracker(3)
        self.play(b1.animate.set_value(-3),run_time=6,rate_func=smooth)
        self.wait()

class ercidingdian06(Scene):
    def construct(self):
        text1 = Text("THANKS FOR WATCHING", font="STSong").shift(UP*1).set_color_by_gradient(RED,BLUE,YELLOW)        
        text2 = Text("POWERED BY MANIM", font="STSong").shift(DOWN*1).set_color(GRAY)
        juxing = Rectangle(height=0.9, width=7.0).move_to(text2).set_color(BLUE)
        self.play(Write(text1))
        self.wait(0.5)
        self.play(LaggedStart(Write(text2),Write(juxing)))
        self.wait()
              
        
        










        




        




