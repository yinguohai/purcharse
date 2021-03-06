# 爬取采购数据

## 包含的功能
+		此爬虫实现了对马帮采购数据的爬取，
+		钉钉机器人自动推送的功能
+		邮件报警功能

### 使用说明：
1. 需要配置 `\conf\config.py` 和 `\controller\email.py` 这两个文件

### config.py 配置文件
```
from datetime import datetime
from collections import OrderedDict
import os

BROWSER = {
    'google' : {
        'download' : os.path.join(os.getcwd(),'excels')
    }
}

ROBOT = {
	#web服务器地址
    'ROBOT_COMMON_URL':'http://xxxxxxxxxxx:83',
    #钉钉机器人地址
	'ROBOT_URL': 'https://xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
}

SINGLE_PATH = os.path.join(os.getcwd(),'single','single.txt')

FILE_MIN_NUM = 0

CURRENT_DATE = datetime.now().strftime('%Y%m%d')

//账号信息
USER_INFO = {
    'username' : 'xxxxxxxxxx',
    'password' : 'xxxxxxxxxxxxxxxxxxxx'
}

PATH_INFO = {
    'login':'http://www.mabangerp.com',
    'purchase':'http://www.mabangerp.com/index.php?mod=main.gotoApp&v=v3&menuKey=M0010703'
}

IS_END = -1

PURCHASE = OrderedDict([
	(3,('purchase_id','采购订单号')),
	(5,('express_id','快递单号')),
	(6,('sku','SKU')),
	(8,('sku_ch','sku中文名')),
	(11,('purchase_num','采购数量')),
	(12,('storage_num','已入库量')),
	(14,('sell_price','采购单价')),
	(15,('one_express_money','运费单价')),
	(16,('express_money','总运费')),
	(17,('discount_amount','折扣')),
	(18,('tax_amount','税金')),
	(19,('amount','总金额')),
	(20,('pre_tax_amount','总金额(税前)')),
	(21,('pre_tax_price','税前单价(税前总金额/采购数量)')),
	(22,('pre_tax_storage_amount','税前入库金额(税前单价*入库数量)')),
	(23,('provider_name','供应商')),
	(24,('provider_address','供应商地址')),
	(26,('remark','备注')),
	(27,('create_time','下单时间')),
	(28,('ali1688_order_id','1688订单号')),
	(29,('developer_name','开发员')),
	(30,('express_type','物流公司')),
	(32,('lower_price','最低采购价')),
	(33,('cost_price','成本价')),
	(34,('product_remark','商品备注')),
	(35,('ali1688_sum_payment','1688实付金额')),
	(36,('create_oper_name','下单员'))
])
```


### 邮件配置文件
```
//邮件服务器地址
self.mail_host = 'smtp.exmail.qq.com'
//邮件服务器登陆名
self.mail_user = 'xxxxxxxxxx'
//登陆密码
self.mail_passwd = 'xxxxxxxxxxxx'
self.mail_port = '465'
//邮件接收人地址
self.receivers = "xxxxxxxxxxxxxx"

```