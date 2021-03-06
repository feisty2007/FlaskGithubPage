$(function() {
        var editor = editormd({
            id   : "editormd",
            placeholder: "just to do it!",
            height: 600,
            // saveHTMLToTextarea : true,
            flowChart : true,
            emoji: true,
            path : "../../static/editormd/lib/",
            imageUpload : true,
            imageFormats : ["jpg", "jpeg", "gif", "png", "bmp", "webp"],
            imageUploadURL : "/uploadfile",
            toolbarIcons: function(){
                return ["undo","redo","|","bold","del","italic","quote","ucwords","uppercase","lowercase","h1","h2","h3","h4","h5","h6",
                    "list-ul","list-ol","table","hr","link","emoji","image","save","||", "watch", "fullscreen", "preview"]
            },
            toolbarIconTexts : {
                save : "保存"  // 如果没有图标，则可以这样直接插入内容，可以是字符串或HTML标签
            },
            toolbarHandlers : {
                save:function(){
                    let title = $("#title").val();
                    let des = $("#des").val();
                    let md_text = editor.getMarkdown();
                    let html_text = editor.getPreviewedHTML();
                    let category = $("select[name='category']").val();
                    let params = {"title":title,
                                  "des":des,
                                  "md_text":md_text,
                                  //"html_text":html_text,
                                  "category":category
                                  };
                    $.ajax({
                        type: "POST",
                        url: "/admin/saveContent",
                        data: params,
                        success: function(res){
                            if(res.code === 0){
                                    layer.alert(res.msg, {icon: 6}, function () {
                                        let index = layer.alert();
                                        layer.close(index);
                                        //window.location.href="/index";
                                    })
                            }else{
                                layer.alert(res.msg, {icon: 5});
                            }
                        },
                        error: function () {
                                        layer.alert('操作失败，网络故障!', {icon: 5});
                                    }
                    })

                }
            }

        });
    });




layui.use(["layer"],function(){
    var layer = layui.layer;
});