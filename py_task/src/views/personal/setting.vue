<route>
{
    meta: {
        title: "个人设置",
        cache: "personal-edit.password"
    }
}
</route>

<script setup name="PersonalSetting">

const router = useRouter()

const form = ref({
    headimg: ''
})

import settingForm from "@/views/personal/setting.form"
const data = ref({
    settingsForm: {
        form: settingForm.form,
        rules: settingForm.rules
    },
    passwordLevel: '强'//密码强度
})
function handleSuccess(res) {
    if (res.error === '') {
        form.value.headimg = res.data.path
    } else {
        ElMessage.warning(res.error)
    }
}
function editPassword() {
    router.push({
        name: 'personalEditPassword'
    })
}
function editEmail() {
    router.push({
        name: 'personalEditEmail'
    })
}
</script>

<template>
    <div>
        <page-main>
            <el-tabs tab-position="left" style="height: 600px;">
                <el-tab-pane label="基本设置" class="basic">
                    <h2>基本设置</h2>
                    <el-row :gutter="20">
                        <el-col :span="16">
                            <el-form ref="formRef" :model="form" :rules="data.settingsForm.rules" label-width="120px" label-suffix="：">
                                <template v-for="(item,index) in data.settingsForm.form" :key="index">
                                    <el-form-item :label="item.label">
                                        <el-input v-model="form[item.name]" :placeholder="item.placeholder" />
                                    </el-form-item>
                                </template>
                                <el-form-item>
                                    <el-button type="primary">保存</el-button>
                                </el-form-item>
                            </el-form>
                        </el-col>
                        <el-col :span="8">
                            <image-upload
                                v-model:url="form.headimg"
                                action="http://scrm.1daas.com/api/upload/upload"
                                name="image" :data="{'token':'TKD628431923530324'}"
                                notip class="headimg-upload"
                                @on-success="handleSuccess"
                            />
                        </el-col>
                    </el-row>
                </el-tab-pane>
                <el-tab-pane label="安全设置" class="security">
                    <h2>安全设置</h2>
                    <div class="setting-list">
                        <div class="item">
                            <div class="content">
                                <div class="title">账户密码</div>
                                <div class="desc">当前密码强度：{{data.passwordLevel}}</div>
                            </div>
                            <div class="action">
                                <el-button text @click="editPassword">修改</el-button>
                            </div>
                        </div>
                        <div class="item">
                            <div class="content">
                                <div class="title">绑定邮箱</div>
                                <div class="desc">{{form.hasOwnProperty('email') ? form.email.substring(0,3)+form.email.substring(4).replace(/^[0-9a-zA-Z]+/,'***'):'当前未绑定邮箱'}}</div>
                            </div>
                            <div class="action">
                                <el-button text @click="editEmail">绑定</el-button>
                            </div>
                        </div>
                    </div>
                </el-tab-pane>
            </el-tabs>
        </page-main>
    </div>
</template>

<style lang="scss" scoped>
:deep(.el-tabs) {
    .el-tabs__header .el-tabs__nav {
        .el-tabs__active-bar {
            z-index: 0;
            width: 100%;
            background-color: var(--el-color-primary-light-9);
            border-right: 2px solid var(--el-color-primary);
            transition: transform 0.3s, background-color 0.3s, var(--el-transition-border);
        }
        .el-tabs__item {
            text-align: left;
            padding-right: 100px;
        }
    }
    .el-tab-pane {
        padding: 0 20px 0 30px;
    }
}
h2 {
    margin: 0;
    margin-bottom: 30px;
    font-weight: normal;
}
.basic {
    :deep(.headimg-upload) {
        text-align: center;
        .el-upload-dragger {
            border-radius: 50%;
        }
    }
}
.security {
    .setting-list {
        .item {
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 10px 0;
            border-bottom: 1px solid var(--el-border-color-lighter);
            transition: var(--el-transition-border);
            .content {
                .title {
                    margin-bottom: 5px;
                    color: var(--el-text-color-primary);
                    transition: var(--el-transition-color);
                }
                .desc {
                    font-size: 14px;
                    color: var(--el-text-color-secondary);
                    transition: var(--el-transition-color);
                }
            }
            &:last-child {
                border-bottom: 0;
            }
        }
    }
}
</style>
