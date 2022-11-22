<route>
{
    meta: {
        title: "修改密码"
    }
}
</route>

<script setup name="PersonalEditPassword">
const route = useRoute(), router = useRouter()
const { proxy } = getCurrentInstance()

import useUserStore from '@/store/modules/user'
const userStore = useUserStore()

const validatePassword = (rule, value, callback) => {
    if (value !== form.value.newpassword) {
        callback(new Error('请确认新密码'))
    } else {
        callback()
    }
}

const formRef = ref()
const form = ref({
    password: '',
    newpassword: '',
    checkpassword: ''
})

const rules = ref({
    password: [
        { required: true, message: '请输入原密码', trigger: 'blur' }
    ],
    newpassword: [
        { required: true, message: '请输入新密码', trigger: 'blur' },
        { min: 6, max: 18, trigger: 'blur', message: '密码长度为6到18位' }
    ],
    checkpassword: [
        { required: true, message: '请输入新密码', trigger: 'blur' },
        { validator: validatePassword }
    ]
})

function onSubmit() {
    formRef.value.validate(valid => {
        if (valid) {
            //修改成功
            ElMessage({
                type: 'success',
                message: '修改成功，请重新登录'
            })
            //跳回登录界面
        }
    })
}
function onCancel() {
    router.push({ name: 'personalSetting' })
}
</script>

<template>
    <div>
        <page-header title="修改密码" content="定期修改密码可以提高帐号安全性噢~" >
            <el-button size="default" round @click="onCancel">
                <template #icon>
                    <el-icon>
                        <svg-icon name="ep:arrow-left" />
                    </el-icon>
                </template>
                返回
            </el-button>
        </page-header>
        <page-main>
            <el-row>
                <el-col :md="24" :lg="12">
                    <el-form ref="formRef" :model="form" :rules="rules" label-width="120px">
                        <el-form-item label="原密码" prop="password">
                            <el-input v-model="form.password" type="password" placeholder="请输入原密码" />
                        </el-form-item>
                        <el-form-item label="新密码" prop="newpassword">
                            <el-input v-model="form.newpassword" type="password" placeholder="请输入原密码" />
                        </el-form-item>
                        <el-form-item label="确认新密码" prop="checkpassword">
                            <el-input v-model="form.checkpassword" type="password" placeholder="请输入原密码" />
                        </el-form-item>
                    </el-form>
                </el-col>
            </el-row>
            <fixed-action-bar>
                <el-button type="default" size="large" @click="onCancel">取消</el-button>
                <el-button type="primary" size="large" @click="onSubmit">提交</el-button>
            </fixed-action-bar>
        </page-main>
    </div>
</template>
