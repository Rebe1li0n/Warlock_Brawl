class AcGame {
    constructor(id){
        //console.log("creat ac Warlock!!");
        this.id = id;
        this.$ac_game = $('#' + id);
        this.menu = new AcGameMenu(this);
        this.playground = new AcGamePlayground(this);


        this.start();
    }


    start() {

    }
}
