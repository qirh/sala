
//[0: anchor_id, 1: iframe_id, 2: string, 3: link, 4: iframe_class]
const top_links = [
    [['anchor_pic_1', 'iframe_pic_1', 'technology', 'photos/tech', 'tech'], ['anchor_pic_1', 'iframe_pic_1', 'technology','photos/tech2', 'tech']],
    [['anchor_pic_2', 'iframe_pic_2', 'travel', 'photos/travel',  'travel'], ['anchor_pic_2', 'iframe_pic_2', 'books', 'photos/books',  'books']],
    [['anchor_pic_3', 'iframe_pic_3', 'two wheeled vehicles','photos/bike',  'bike'], ['anchor_pic_3', 'iframe_pic_3', 'two wheeled vehicles','photos/bike2', 'bike2']],
    [['anchor_pic_4', '', 'handsome', 'photos/moi-moustache', ''], ['anchor_pic_4', '', 'handsome', 'photos/moi-sans-moustache', '']]
];
function create_random_pair() {
    top_links.forEach(function (element) {
        var selection = element[Math.floor((Math.random() * 2))];
        var document_selection = document.getElementById(selection[0]);
        if (selection[1] != '') {
            document_selection.innerHTML = selection[2] + '<iframe id="' + selection[1] + '" class="popup ' + selection[4] + '" src="/static/' + selection[3] + '.jpg" type="image/jpeg"></iframe>';
            document_selection.href = selection[3];
        }
        else {
            document_selection.innerHTML = selection[2];
            document_selection.href = selection[3];
        }
    })
}
document.addEventListener('DOMContentLoaded', function() {create_random_pair();}, false);
