
function getRandomColor(){
    return  "#000000".replace(/0/g,function(){
        return (~~(Math.random()*16)).toString(16);});
    }
function ran_col() { //function name
    const class_list = document.getElementsByClassName('card-head');

    for (var i = 0; i < class_list.length; i++) {
        class_list[i].style.background = 'linear-gradient('+(Math.random()*360)+'deg,'+ getRandomColor()+ ' 0%,'+getRandomColor()+ ' 100%)';
    }

    const class_list_show = document.getElementsByClassName('card-head-show');
    for (var i = 0; i < class_list_show.length; i++) {
        class_list_show[i].style.background = 'linear-gradient('+(Math.random()*360)+'deg,'+ getRandomColor()+ ' 0%,'+getRandomColor()+ ' 100%)';
    }
}