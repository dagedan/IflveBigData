const nav =  {
    name: 'nav-bar',
    data() {
        return {
            scrollTop: 0,
            showBorder: false
        }
    },
    mounted() {
        let _this = this
        this.$nextTick(() => {
            document.onscroll = function() {
                _this.scrollTop = document.documentElement.scrollTop || document.body.scrollTop || window.pageYOffset
                if (_this.scrollTop != 0) {
                    _this.showBorder = true
                } else {
                    _this.showBorder = false
                }
            }
        })
    },
    methods: {
        toHomePage () {
            location.href='/'
        },
    },
    template: `
    <div class="nav" @click="toHomePage" :class="{'nav-border':showBorder}">
        <img src="./static/images/logo.png" class="logo_short" style="margin-left:20px">
        <div class="split_v"></div>
        <img src="./static/images/logo1.jpg" class="logo_short">
        <div class="split_v"></div>
        <img src="./static/images/logo3.png" class="logo_long">
        <div class="split"></div>
        <a href="/signup">注册</a>
        <div class="split_v" style="margin: 0px 20px;"></div>
        <a style="margin-right: 50px;" href="/login">登陆</a>
    </div>`
}
