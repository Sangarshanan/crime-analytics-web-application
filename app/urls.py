from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.redi , name = 'redi'),
    url(r'^index', views.login , name = 'login'),
    url(r'^login/$', views.login , name = 'login'),
    url(r'^register', views.register , name = 'register'),
    url(r'^page1', views.page1 , name = 'page1'),
    url(r'^overyears', views.wrtstate , name = 'wrtstate'),
    url(r'^murders', views.murders , name = 'murders'),
    url(r'^chart2001', views.chart2001 , name = 'chart2001'),
    url(r'^chart2002', views.chart2002 , name = 'chart2002'),
    url(r'^chart2003', views.chart2003 , name = 'chart2003'),
    url(r'^chart2004', views.chart2004 , name = 'chart2004'),
    url(r'^chart2005', views.chart2005 , name = 'chart2005'),
    url(r'^chart2006', views.chart2006 , name = 'chart2006'),
    url(r'^chart2007', views.chart2007 , name = 'chart2007'),
    url(r'^chart2008', views.chart2008 , name = 'chart2008'),
    url(r'^chart2009', views.chart2009 , name = 'chart2009'),
    url(r'^chart2010', views.chart2010 , name = 'chart2010'),
    url(r'^pie2001', views.pie2001 , name = 'pie2001'),
    url(r'^pie2002', views.pie2002 , name = 'ddds'),
    url(r'^pie2003', views.pie2003 , name = 'sdf'),
    url(r'^pie2004', views.pie2004 , name = 'mzzm'),
    url(r'^pie2005', views.pie2005 , name = 'amm'),
    url(r'^pie2006', views.pie2006 , name = 'mdmsd'),
    url(r'^pie2007', views.pie2007 , name = 'sms'),
    url(r'^pie2008', views.pie2008 , name = 'smsss'),
    url(r'^pie2009', views.pie2009 , name = 'lvl'),
    url(r'^pie2010', views.pie2010 , name = 'trr'),
    url(r'^murdpie2001', views.murdpie2001 , name = 'murdpie2001'),
    url(r'^murdpie2002', views.murdpie2002 , name = 'murdpie2002'),
    url(r'^murdpie2003', views.murdpie2003 , name = 'murdpie2003'),
    url(r'^murdpie2004', views.murdpie2004 , name = 'murdpie2004'),
    url(r'^murdpie2005', views.murdpie2005 , name = 'murdpie2005'),
    url(r'^murdpie2006', views.murdpie2006 , name = 'murdpie2006'),
    url(r'^murdpie2007', views.murdpie2007 , name = 'murdpie2007'),
    url(r'^murdpie2008', views.murdpie2008 , name = 'murdpie2008'),
    url(r'^murdpie2009', views.murdpie2009 , name = 'murdpie2009'),
    url(r'^murdpie2010', views.murdpie2010 , name = 'murdpie2010'),
    url(r'^murd2010', views.murd2010 , name = 'murd2010'),
    url(r'^murd2001', views.murd2001 , name = 'murd2001'),
    url(r'^murd2002', views.murd2002 , name = 'murd2002'),
    url(r'^murd2003', views.murd2003 , name = 'murd20103'),
    url(r'^murd2004', views.murd2004 , name = 'murd201022'),
    url(r'^murd2005', views.murd2005 , name = 'murd2010we'),
    url(r'^murd2006', views.murd2006 , name = 'murd2010weqw'),
    url(r'^murd2007', views.murd2007 , name = 'murd2010wrar'),
    url(r'^murd2008', views.murd2008 , name = 'murd201011'),
    url(r'^murd2009', views.murd2009 , name = 'murd2010emke'),
    url(r'^shooting', views.shooting , name = 'shooting'),
    url(r'^shot_kil', views.shot_kil , name = 'shot_kil'),
    url(r'^shot_inj', views.shot_inj , name = 'shot'),
    url(r'^injkill', views.injkill , name = 'shotkill'),
    url(r'^fatal', views.fatal , name = 'fatal'),
    url(r'^death', views.death , name = 'death'),
    url(r'^inj', views.inj , name = 'inj'),
    url(r'^diainj', views.diainj , name = 'diainj'),
    url(r'^deaandinj', views.deaandinj , name = 'deaandinj'),
    url(r'^formcrimesagaintswomen', views.add , name = 'add_model'),
    url(r'^formmurder', views.addmv , name = 'addmv'),
    url(r'^sanfrancisco', views.sss , name = 'sanfrancisco'),












    












]
