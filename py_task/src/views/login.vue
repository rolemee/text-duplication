<route>
{
    meta: {
        title: "登录",
        constant: true,
        layout: false
    }
}
</route>

<script setup name="Login">
const { proxy } = getCurrentInstance()
const route = useRoute(), router = useRouter()

import useSettingsStore from '@/store/modules/settings'
const settingsStore = useSettingsStore()
import useUserStore from '@/store/modules/user'
const userStore = useUserStore()

// const banner = new URL('../assets/images/login-banner.png', import.meta.url).href
const title = import.meta.env.VITE_APP_TITLE

// 表单类型，login 登录，reset 重置密码
const formType = ref('login')

// 登录
const loginForm = ref({
    account: localStorage.login_account || '',
    password: ''
})
const loginRules = ref({
    account: [
        { required: true, trigger: 'blur', message: '请输入用户名' }
    ],
    password: [
        { required: true, trigger: 'blur', message: '请输入密码' },
    ]
})

const loginFormRef = ref()
function handleLogin() {
    loginFormRef.value.validate(valid => {
        if (valid) {
            loading.value = true
            userStore.login(loginForm.value).then(() => {
                loading.value = false
                router.push(redirect.value)
            }).catch(() => {
                loading.value = false
            })
        }
    })
}

const loading = ref(false)
const passwordType = ref('password')
const redirect = ref(null)

onMounted(() => {
    redirect.value = route.query.redirect ?? '/'
})

function showPassword() {
    passwordType.value = passwordType.value === 'password' ? '' : 'password'
    nextTick(() => {
        proxy.$refs.password.focus()
    })
}

</script>

<template>
    <div>
        <div class="bg-banner" />
        <div id="login-box">
            <el-form v-show="formType === 'login'" ref="loginFormRef" :model="loginForm" :rules="loginRules" class="login-form" autocomplete="on">
                <div class="title-container">
                    <h3 class="title">欢迎来到 {{ title }} ! 👋🏻</h3>
                </div>
                <div>
                    <el-form-item prop="account">
                        <el-input ref="name" v-model="loginForm.account" placeholder="用户名" text tabindex="1" autocomplete="on">
                            <template #prefix>
                                <el-icon>
                                    <svg-icon name="user" />
                                </el-icon>
                            </template>
                        </el-input>
                    </el-form-item>
                    <el-form-item prop="password">
                        <el-input ref="password" v-model="loginForm.password" :type="passwordType" placeholder="密码" tabindex="2" autocomplete="on" @keyup.enter="handleLogin">
                            <template #prefix>
                                <el-icon>
                                    <svg-icon name="password" />
                                </el-icon>
                            </template>
                            <template #suffix>
                                <el-icon>
                                    <svg-icon :name="passwordType === 'password' ? 'eye' : 'eye-open'" @click="showPassword" />
                                </el-icon>
                            </template>
                        </el-input>
                    </el-form-item>
                </div>
                <el-button :loading="loading" type="primary" size="large" style="width: 100%;" @click.prevent="handleLogin">登录</el-button>
            </el-form>
        </div>
        <Copyright v-if="settingsStore.copyright.enable" />
    </div>
</template>

<style lang="scss" scoped>
[data-mode="mobile"] {
    #login-box {
        position: relative;
        width: 100%;
        height: 100%;
        top: inherit;
        left: inherit;
        transform: translateX(0) translateY(0);
        flex-direction: column;
        justify-content: start;
        border-radius: 0;
        box-shadow: none;
        .login-form {
            width: 100%;
            min-height: auto;
            padding: 30px;
        }
    }
    .copyright {
        position: relative;
        bottom: 0;
        padding-bottom: 10px;
    }
}
:deep(input[type="password"]::-ms-reveal) {
    display: none;
}
.bg-banner {
    position: fixed;
    z-index: 0;
    width: 100%;
    height: 100%;
    background: url('@/assets/images/background-image.jpg') no-repeat center center;
    background-size: cover;
}
#login-box {
    display: flex;
    justify-content: space-between;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translateX(-50%) translateY(-50%);
    background-color: var(--el-bg-color);
    opacity: 0.8;
    border-radius: 10px;
    overflow: hidden;
    box-shadow: var(--el-box-shadow);
    .login-form {
        display: flex;
        flex-direction: column;
        justify-content: center;
        min-height: 500px;
        width: 500px;
        padding: 50px;
        overflow: hidden;
        .title-container {
            position: relative;
            .title {
                font-size: 1.3em;
                color: var(--el-text-color-primary);
                margin: 0 auto 30px;
                font-weight: bold;
            }
        }
    }
    .el-form-item {
        margin-bottom: 24px;
        :deep(.el-input) {
            height: 48px;
            line-height: inherit;
            width: 100%;
            input {
                height: 48px;
            }
            .el-input__prefix,
            .el-input__suffix {
                display: flex;
                align-items: center;
            }
            .el-input__prefix {
                left: 10px;
            }
            .el-input__suffix {
                right: 10px;
            }
        }
    }
}
.copyright {
    position: absolute;
    bottom: 30px;
    width: 100%;
    margin: 0;
}
</style>
