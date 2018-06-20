
//[0: anchor_id, 1: iframe_id, 2: string, 3: link, 4: iframe_class]
const top_links = [
    [['anchor_pic_1', 'iframe_pic_1', 'التقنية', 'photos/tech', 'tech'], ['anchor_pic_1', 'iframe_pic_1', 'التقنية','photos/tech2', 'tech2']],
    [['anchor_pic_2', 'iframe_pic_2', 'السفر', 'photos/travel',  'travel'], ['anchor_pic_2', 'iframe_pic_2', 'القراءة', 'photos/books',  'books']],
    [['anchor_pic_3', 'iframe_pic_3', 'الدراجات','photos/bike',  'bike'], ['anchor_pic_3', 'iframe_pic_3', 'الدراجات','photos/bike2', 'bike2']],
    [['anchor_pic_4', '', 'أنا', 'photos/moi-moustache', ''], ['anchor_pic_4', '', 'أنا', 'photos/moi-sans-moustache', '']]
];
function create_random_pair() {
    top_links.forEach(function (element) {
        var selection = element[Math.floor((Math.random() * 2))];
        var document_selection = document.getElementById(selection[0]);
        if (selection[1] != '') {

            document_selection.innerHTML = selection[2] + '<embed id="' + selection[1] + '" class="popup ' + selection[4] + '" src="/static/' + selection[3] + '.jpg" type="image/jpeg"></embed>';
            document_selection.href = selection[3];
        }
        else {
            document_selection.innerHTML = selection[2];
            document_selection.href = selection[3];
        }
    })
}
document.addEventListener('DOMContentLoaded', function() {create_random_pair();}, false);
