import sys
import os
sys.path.insert(0, os.getcwd())

from api.models import session
from api.models.models import Prefecture

prefectures = (
    Prefecture(prefName="愛知県"),
    Prefecture(prefName="秋田県"),
    Prefecture(prefName="青森県"),
    Prefecture(prefName="千葉県"),
    Prefecture(prefName="愛媛県"),
    Prefecture(prefName="福井県"),
    Prefecture(prefName="福岡県"),
    Prefecture(prefName="福島県"),
    Prefecture(prefName="岐阜県"),
    Prefecture(prefName="群馬県"),
    Prefecture(prefName="広島県"),
    Prefecture(prefName="北海道"),
    Prefecture(prefName="兵庫県"),
    Prefecture(prefName="茨城県"),
    Prefecture(prefName="石川県"),
    Prefecture(prefName="岩手県"),
    Prefecture(prefName="香川県"),
    Prefecture(prefName="鹿児島県"),
    Prefecture(prefName="神奈川県"),
    Prefecture(prefName="高知県"),
    Prefecture(prefName="熊本県"),
    Prefecture(prefName="京都府"),
    Prefecture(prefName="三重県"),
    Prefecture(prefName="宮城県"),
    Prefecture(prefName="宮崎県"),
    Prefecture(prefName="長野県"),
    Prefecture(prefName="長崎県"),
    Prefecture(prefName="奈良県"),
    Prefecture(prefName="新潟県"),
    Prefecture(prefName="大分県"),
    Prefecture(prefName="岡山県"),
    Prefecture(prefName="沖縄県"),
    Prefecture(prefName="大阪府"),
    Prefecture(prefName="佐賀県"),
    Prefecture(prefName="埼玉県"),
    Prefecture(prefName="滋賀県"),
    Prefecture(prefName="島根県"),
    Prefecture(prefName="静岡県"),
    Prefecture(prefName="栃木県"),
    Prefecture(prefName="徳島県"),
    Prefecture(prefName="東京都"),
    Prefecture(prefName="鳥取県"),
    Prefecture(prefName="富山県"),
    Prefecture(prefName="和歌山県"),
    Prefecture(prefName="山形県"),
    Prefecture(prefName="山口県"),
    Prefecture(prefName="山梨県"),
    Prefecture(prefName="その他"),
)

session.add_all(prefectures)
session.commit()
