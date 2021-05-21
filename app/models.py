from django.db import models
from users.models import User
from django.core import validators

class Dantai(models.Model):
    """
    団体マスタ定義クラス

    顧客所属の団体マスタを定義します。
    """

    name = models.CharField(
        verbose_name='団体マスタ',
        max_length=50,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name

        
    class Meta:
        """
        管理画面でのタイトル表示
        """
        verbose_name = '所属団体マスタ'
        verbose_name_plural = '所属団体マスタ'

class Item(models.Model):
    """
    データ定義クラス
      各フィールドを定義する
    参考：
    ・公式 モデルフィールドリファレンス
    https://docs.djangoproject.com/ja/2.1/ref/models/fields/
    """

    name = models.CharField(
        verbose_name='顧客名',
        max_length=20,
        blank=True,
        null=True,
    )

    name_furigana = models.CharField(
        verbose_name='フリガナ',
        max_length=20,
        blank=True,
        null=True,
        default='',
        validators=[validators.RegexValidator(
            regex=u'^[ァ-ヶ]+$',
            message='全角フリガナで入力してください',
        )]
    )

    address = models.CharField(
        verbose_name='住所',
        max_length=40,
        blank=True,
        null=True,
    )

    email = models.EmailField(
        verbose_name='メール',
        max_length=100,
        blank=True,
        null=True,
    )
    
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

    todofuken = models.IntegerField(
        verbose_name='都道府県',
        choices=todofukenChoice,
        blank=True,
        null=True,
    )

    # サンプル項目9 選択肢（マスタ連動）
    Dantai = models.ForeignKey(
        Dantai,
        verbose_name='所属団体（マスタ連動）',
        blank=True,
        null=True,
        related_name='Dantai',
        on_delete=models.SET_NULL,
    ) 

    leaseDate = models.DateField(
        verbose_name='リース期限',
        blank=True,
        null=True,
    )

    onlineSupport = models.BooleanField(
        verbose_name='オンラインサポート',
    )

    hpUrl = models.URLField(
        verbose_name='HPのURL',
        max_length=100,
        blank=True,
        null=True,
    )

    memo = models.TextField(
        verbose_name='メモ',
        blank=True,
        null=True,
    )

    # # サンプル項目1 文字列
    # CustomerName = models.CharField(
    #     verbose_name='顧客名',
    #     max_length=20,
    #     blank=True,
    #     null=True,
    # )

    # # サンプル項目2 メモ
    # sample_2 = models.TextField(
    #     verbose_name='サンプル項目2 メモ',
    #     blank=True,
    #     null=True,
    # )

    # # サンプル項目3 整数
    # sample_3 = models.IntegerField(
    #     verbose_name='サンプル項目3 整数',
    #     blank=True,
    #     null=True,
    # )

    # # サンプル項目4 浮動小数点
    # sample_4 = models.FloatField(
    #     verbose_name='サンプル項目4 浮動小数点',
    #     blank=True,
    #     null=True,
    # )

    # # サンプル項目5 固定小数点
    # sample_5 = models.DecimalField(
    #     verbose_name='サンプル項目5 固定小数点',
    #     max_digits=5,
    #     decimal_places=2,
    #     blank=True,
    #     null=True,
    # )

    # # サンプル項目6 ブール値
    # sample_6 = models.BooleanField(
    #     verbose_name='サンプル項目6 ブール値',
    # )

    # # サンプル項目7 日付
    # sample_7 = models.DateField(
    #     verbose_name='サンプル項目7 日付',
    #     blank=True,
    #     null=True,
    # )

    # # サンプル項目8 日時
    # sample_8 = models.DateTimeField(
    #     verbose_name='サンプル項目8 日時',
    #     blank=True,
    #     null=True,
    # )

    # # サンプル項目9 選択肢（固定）
    # sample_9_choice = (
    #     (1, '選択１'),
    #     (2, '選択２'),
    #     (3, '選択３'),
    # )

    # sample_9 = models.IntegerField(
    #     verbose_name='サンプル項目9_選択肢（固定）',
    #     choices=sample_9_choice,
    #     blank=True,
    #     null=True,
    # )

    # # サンプル項目9 選択肢（マスタ連動）
    # sample_10 = models.ForeignKey(
    #     User,
    #     verbose_name='サンプル項目10_選択肢（マスタ連動）',
    #     blank=True,
    #     null=True,
    #     related_name='sample_10',
    #     on_delete=models.SET_NULL,
    # )

    # 以下、管理項目

    # 作成者(ユーザー)
    created_by = models.ForeignKey(
        User,
        verbose_name='作成者',
        blank=True,
        null=True,
        related_name='CreatedBy',
        on_delete=models.SET_NULL,
        editable=False,
    )

    # 作成時間
    created_at = models.DateTimeField(
        verbose_name='作成時間',
        blank=True,
        null=True,
        editable=False,
    )

    # 更新者(ユーザー)
    updated_by = models.ForeignKey(
        User,
        verbose_name='更新者',
        blank=True,
        null=True,
        related_name='UpdatedBy',
        on_delete=models.SET_NULL,
        editable=False,
    )

    # 更新時間
    updated_at = models.DateTimeField(
        verbose_name='更新時間',
        blank=True,
        null=True,
        editable=False,
    )

    def __str__(self):
        """
        リストボックスや管理画面での表示
        """
        return self.name

    class Meta:
        """
        管理画面でのタイトル表示
        """
        verbose_name = '顧客マスタ'
        verbose_name_plural = '顧客マスタ'

