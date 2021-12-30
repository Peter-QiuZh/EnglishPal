# EnglishPal - Learn English Words Smartly

## Improvements
- 将“登出”按钮改为“退出”
- 将“粘帖”改为“粘贴”
- 在“我的生词薄”中，当用户点击“熟悉”或“不熟悉”按钮时，不会重新刷新整个页面而回到页面的顶部，而是采取异步的方式局部刷新数据
Demo video link: https://www.bilibili.com/video/BV1SY411H7sb/

## Code Modification
1.整个项目中加入了jquery.js
2.修改了main.py的familiar和unfamiliar方法的返回类型：
- original: return redirect(url_for('userpage', username=username))
- now: return "success"
3.在main.py的userpage方法中，当请求为"GET"时进行了如下修改：
- 添加了script脚本：
  page += '<script type="text/javascript" src="static/js/jquery.js"></script>'
          page += '''
                   <script>
                       $(function(){
                          familiar(index);
                          unfamiliar(index);
                       });
                       function familiar(index) {
                          var username = $("#username").text();
                          var word = $("#word_" + index).text();
                          var freq = $("#freq_" + index).text();
                          $.ajax({
                              type:"get",
                              url:"/" + username + "/" + word + "/familiar",
                              success:function(resp){
                                  var new_freq = freq - 1;
                                  if(new_freq <1) {
                                      $("#p_" + index).remove();
                                  } else {
                                      $("#freq_" + index).text(new_freq);
                                  }
                              }
                          });
                       }
                       function unfamiliar(index) {
                          var username = $("#username").text();
                          var word = $("#word_" + index).text();
                          var freq = $("#freq_" + index).text();
                          $.ajax({
                              type:"get",
                              url:"/" + username + "/" + word + "/unfamiliar",
                              success:function(resp){
                                  var new_freq = parseInt(freq) + 1;
                                  $("#freq_" + index).text(new_freq);
                              }
                          });
                       }
                   </script>
                  '''
- 为<p>标签，“熟悉”和“不熟悉”按钮添加了id：
  page += '<p id="p_%d" class="new-word" > <a class="btn btn-light" id="word_%d" href="%s" role="button">%s</a>(<a id="freq_%d" title="%s" >%d</a>) <a class="btn btn-success" href="javascript:void(0);" onclick="familiar(%d)" role="button">熟悉</a> <a class="btn btn-warning" href="javascript:void(0);" onclick="unfamiliar(%d)" role="button">不熟悉</a> <a class="btn btn-danger" href="del(%d)" role="button">删除</a> </p>\n ' % (sorted_lst.index(x), sorted_lst.index(x), youdao_link(word), word, sorted_lst.index(x), '; '.join(d[word]), freq, sorted_lst.index(x), sorted_lst.index(x), sorted_lst.index(x))
