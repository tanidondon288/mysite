$(function () {

    // jQueryコード

    // 時間系フィールドにはbootstrap-datepickerよbootstrap-datetimepickerの利用を推奨します。
    // 参考 https://pypi.org/project/django-tempus-dominus/


    // Bootstrap Datepicker
    $('.dateinput').datepicker({
        todayBtn: 'linked',
        format: 'yyyy-mm-dd',
        language: 'ja',
        autoclose: true,
        todayHighlight: true,
    });
    $('.dateinput').attr('placeholder','YYYY-MM-DD');

    $('.datetimeinput').attr('placeholder','YYYY-MM-DD HH:MM:SS');


    // 入力フォームでリターンキー押下時の送信を無効化
    // ※フィールド１個の時は無効
    $('#myform').on('sumbit', function (e) {
        e.preventDefault();
    })

    // 送信ボタンの２度押しを防止
    $('.save').on('click', function (e) {
        $('.save').addClass('disabled');
        $('#myform').submit();
    })

    // 削除ボタンの２度押しを防止
    $('.delete').on('click', function (e) {
        $('.delete').addClass('disabled');
    })

    // [検索を解除] の表示制御
    //
    // 検索フォーム内の項目が一つでも入力されていたら、検索中と見なし
    // [検索を解除]のボタンを有効化する。
    //
    let conditions = $('#filter').serializeArray();
    $.each(conditions, function () {

        // boolフィールドの検索欄は、デフォルトが「1:不明」なので特別扱い
        if ($('[name=' + this.name + ']').hasClass('nullbooleanselect') && this.value == 1) {
            return;
        }

        // その他の項目はnull,'',0,Falseをもって未入力とみなす。
        if (this.value) {
            $('.filtered').css('visibility', 'visible');
        }
    })

    // ページネーションのレスポンシブ対応
    // jQuery Plugin rPageを利用
    // https://auxiliary.github.io/rpage/
    $(".pagination").rPage();


    //カタカナチェック（未完成）
    //$("input[name='name_furigana']").blur(function(){
    //    if(!$(this).val().match(/^[ァ-ヶ　\r\n\t]*$/)){
    //    //実行内容
    //        $("input[name='name_furigana']").append("あああカタカナ以外が入力されています。<br>");
    //    }
    //  });

    //jquery.autoKanaの自動ふりがな・カタカナ入力対応
    $.fn.autoKana('#id_name', '#id_name_furigana', {
        katakana : true
    });

    //ページ移動時にアラート出す
    changeFlg = false;
    $("form input, form textarea, form select").change(function() {
        changeFlg = true;
    });
    $('.save').click(function() {
        changeFlg = false;
    });
    $(window).on('beforeunload', function() {
        if (changeFlg) {
            return "ページを移動しようとしています。\n入力した内容が失われますがよろしいですか？";
        }
    });

    //（未完成）スマホ用「ページ移動時にアラート出す」
    //var hash = location.hash;
    //if(hash != '#message') {
    //  // pushStateで現在のURLを履歴にスタックする
    //  history.pushState(null,null,location.href);
    //  // URLにtagを設置する
    //  location.hash = '#message';
    //}
    //// URLが変更されるのを監視
    //$(window).on('save',function(event){
    //  if(location.hash != '#message') {
    //    // モーダルを実行
    //    $('#modal').modal('show');
    //  }
    //});
    //$('#back').click(function() {
    //  history.back();
    //  return false;
    //});

    //フローティングラベル
    $('.textinput').on('input', function() {
        var $field = $(this).closest('.form-group');
        if (this.value) {
          $field.addClass('not-empty');
        } else {
          $field.removeClass('not-empty');
        }
      });


});