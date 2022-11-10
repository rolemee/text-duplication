import api from '@/api'

import useRouteStore from './route'
import useMenuStore from './menu'
import {ElMessage} from "element-plus";

const useUserStore = defineStore(
    // 唯一ID
    'user',
    {
        state: () => ({
            account: localStorage.account || '',
            userId: localStorage.userId || '',
            token: localStorage.token || '',
            permissions: []
        }),
        getters: {
            isLogin: state => {
                let retn = false
                if (state.token) {
                    retn = true
                }
                return retn
                // return true
            }
        },
        actions: {
            login(data) {
                return new Promise((resolve, reject) => {
                    api.post('/login', data).then(res => {
                        document.cookie = 'session=' + res.data.session
                        this.token = res.data.session
                        this.userId = data.account
                        localStorage.setItem('userId' , data.account)
                        localStorage.setItem('token', res.data.session)
                        api.post('/userInfo', {
                            usernameId: data.account
                        }).then(res => {
                            localStorage.setItem('account', res.data.name)
                            this.account = res.data.name
                            resolve()
                        })
                    }).catch(error => {
                        reject(error)
                    })
                })
            },
            logout() {
                return new Promise(resolve => {
                    const routeStore = useRouteStore()
                    const menuStore = useMenuStore()
                    localStorage.removeItem('account')
                    localStorage.removeItem('token')
                    this.account = ''
                    this.token = ''
                    this.userId = ''
                    this.permissions = []
                    routeStore.removeRoutes()
                    menuStore.setActived(0)
                    resolve()
                })
            },
            getPermission() {
                return new Promise(resolve => {
                    api.post('/userInfo', {
                        usernameId: this.userId
                    }).then(res => {
                        // console.log(res)
                        this.permissions.push(res.data.rights)
                        resolve(this.permissions)
                    }).catch(error => {
                        ElMessage.error('登录信息已过期,请重新登录')
                        console.log(error)
                        resolve([])
                    })
                })

            }
        }
    }
)

export default useUserStore
