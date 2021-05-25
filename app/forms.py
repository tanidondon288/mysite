from django import forms
from .models import Item
from .models import Dantai

"""
todofukenChoice = (
        (1, '北海道'),
        (2, '青森県'),
        (3, '岩手県'),
        (4, '宮城県'),
        (5, '秋田県'),
        (6, '山形県'),
        (7, '福島県'),
        (8, '茨城県'),
        (9, '栃木県'),
        (10, '群馬県'),
        (11, '埼玉県'),
        (12, '千葉県'),
        (13, '東京都'),
        (14, '神奈川県'),
        (15, '新潟県'),
        (16, '富山県'),
        (17, '石川県'),
        (18, '福井県'),
        (19, '山梨県'),
        (20, '長野県'),
        (21, '岐阜県'),
        (22, '静岡県'),
        (23, '愛知県'),
        (24, '三重県'),
        (25, '滋賀県'),
        (26, '京都府'),
        (27, '大阪府'),
        (28, '兵庫県'),
        (29, '奈良県'),
        (30, '和歌山県'),
        (31, '鳥取県'),
        (32, '島根県'),
        (33, '岡山県'),
        (34, '広島県'),
        (35, '山口県'),
        (36, '徳島県'),
        (37, '香川県'),
        (38, '愛媛県'),
        (39, '高知県'),
        (40, '福岡県'),
        (41, '佐賀県'),
        (42, '長崎県'),
        (43, '熊本県'),
        (44, '大分県'),
        (45, '宮崎県'),
        (46, '鹿児島県'),
        (47, '沖縄県 '),
)
"""

class ItemForm(forms.ModelForm):
    """
    モデルフォーム構成クラス
    ・公式 モデルからフォームを作成する
    https://docs.djangoproject.com/ja/2.1/topics/forms/modelforms/
    """

#    address1 = forms.MultipleChoiceField(
#        label='都道府県5テスト',
#        widget=forms.CheckboxSelectMultiple,
#        choices=todofukenChoice,
#        required=False,
#    )

#    aiueo = forms.ChoiceField(
#        label='都道府県2',
#        widget=forms.Select,
#        choices=todofukenChoice,
#        required=False,
#    )

#    kaki = forms.ModelChoiceField (
#        Dantai,
#        label='所属団体form改変',
#        widget=forms.RadioSelect,
#        required=False,
#    )

#    sashi = forms.MultipleChoiceField(
#        label='都道府県4',
#        choices=todofukenChoice,
#        required=False,
#    )

#    tachi = forms.MultipleChoiceField(
#        label='都道府県5',
#        widget=forms.CheckboxSelectMultiple,
#        choices=todofukenChoice,
#        required=False,
#    )

    name_furigana = forms.CharField(
        label='フリガナ',
        max_length=20,
        required=False,
        help_text="全角フリガナ20文字以内で入力して下さい",
        widget=forms.TextInput(attrs={'placeholder':'フリガナ'}),
    )

    postcode = forms.RegexField(
        label='郵便番号',
        regex=r'^[0-9]+$',
        required=False,
        max_length=7,
        widget=forms.TextInput(attrs={'onKeyUp' : "AjaxZip3.zip2addr('postcode','','address1','address2')",'placeholder':'郵便番号'}),
        help_text="半角数字7文字（ハイフン「-」無し）で入力して下さい",
    )

    class Meta:
        model = Item
        fields = '__all__'

        widgets = {
            'name':forms.TextInput(attrs={'placeholder':'顧客名'}),
            'address2':forms.TextInput(attrs={'placeholder':'市町村番地'}),
            'address3':forms.TextInput(attrs={'placeholder':'建物名'}),
            'email':forms.EmailInput(attrs={'placeholder':'メールアドレス'}),
            'hpUrl':forms.URLInput(attrs={'placeholder':'例：http://abc.co.jp、https://abc.com'}),
        }

        #削除予定
        #labels = {
        #    'address3':'テストテスト',
        #}


        ##ForeignKeyのモデル項目の形式を変更した場合は以下を使う。（モデルフォームなのでclass Meta内で行うようにする）
        #widgets = {
        #    'Dantai' : forms.RadioSelect
        #}


        # 以下のフィールド以外が入力フォームに表示される
        # AutoField
        # auto_now=True
        # auto_now_add=Ture
        # editable=False
