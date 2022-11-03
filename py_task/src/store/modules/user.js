import api from '@/api'

import useRouteStore from './route'
import useMenuStore from './menu'

const useUserStore = defineStore(
    // 唯一ID
    'user',
    {
        state: () => ({
            account: localStorage.account || '',
            token: localStorage.token || '',
            permissions: []
        }),
        getters: {
            isLogin: state => {
                // let retn = false
                // if (state.token) {
                //     retn = true
                // }
                // return retn
                return true
            }
        },
        actions: {
            login(data) {
                return new Promise((resolve, reject) => {
                    api.post('/login', data).then(res => {
                        document.cookie = 'session=' + res.data.session
                        localStorage.setItem('account', res.data.account)
                        localStorage.setItem('token', res.data.session)
                        this.account = res.data.account
                        this.token = res.data.token
                        resolve()
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
                    routeStore.removeRoutes()
                    menuStore.setActived(0)
                    resolve()
                })
            },
            // 获取我的权限
            getPermissions() {
                return new Promise(resolve => {
                    // 通过 mock 获取权限
                    api.get('member/permission', {
                        baseURL: '/mock/',
                        params: {
                            account: this.account
                        }
                    }).then(res => {
                        this.permissions = res.data.permissions
                        resolve(res.data.permissions)
                    })
                })
            }
        }
    }
)

export default useUserStore
