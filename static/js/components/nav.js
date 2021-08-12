const nav =  {
    name: 'nav-bar',
    data() {
        return {
            scrollTop: 0,
            showBorder: false,
            username: Cookies.get('username')
        }
    },
    mounted() {
        console.log('Cookies:', Cookies)
        window.Cookies = Cookies
        console.log('type:', this.username)
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
        <div v-if="!username" style="display:flex">
            <a href="/signup">注册</a>
            <div style="width: 1px;height: 20px;border-left: 1px solid #303133;margin:0px 20px"></div>
            <a style="margin-right: 50px;" href="/login">登陆</a>
        </div>
        <div v-else style="display:flex;align-items:center;margin-right: 50px;">
            <div class="username">{{username}}
                <div class="level-tip">奠基用户</div>
            </div>
<!--            <a class="c-a" href="/logout" style="margin-right: 15px">进入管理后台</a>-->
<!--            <a class="c-a" href="/logout">退出登陆</a>-->
        </div>
    </div>`
}
