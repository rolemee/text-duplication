<script setup>
import DetailForm from '../DetailForm/index.vue'

const { proxy } = getCurrentInstance()

const props = defineProps({
    // eslint-disable-next-line vue/valid-define-props
    ...DetailForm.props,
    modelValue: {
        type: Boolean,
        default: false
    },
    mode: {
        type: String,
        default: 'dialog',
        validator: val => ['dialog', 'drawer'].includes(val)
    },
    title: {
        type: String,
        default: '',
        // required: true
    }
})

const emit = defineEmits(['update:modelValue', 'success'])

let myVisible = computed({
    get: function() {
        return props.modelValue
    },
    set: function(val) {
        emit('update:modelValue', val)
    }
})

const title = computed(() => props.title ? props.title : 'test')

function onSubmit() {
    // submit() 为组件内部方法
    proxy.$refs['form'].submit(() => {
        emit('success')
        onCancel()
    })
}

function onCancel() {
    myVisible.value = false
}
</script>

<template>
    <div>
        <el-dialog v-if="props.mode === 'dialog'" v-model="myVisible" :title="title" width="600px" :close-on-click-modal="false" append-to-body destroy-on-close>
            <DetailForm ref="form" v-bind="$props" />
            <template #footer v-if="props.type !== 'view'">
                <el-button size="large" @click="onCancel">取 消</el-button>
                <el-button type="primary" size="large" @click="onSubmit">确 定</el-button>
            </template>
        </el-dialog>
        <el-drawer v-else-if="props.mode === 'drawer'" v-model="myVisible" :title="title" size="600px" :close-on-click-modal="false" destroy-on-close>
            <DetailForm ref="form" v-bind="$props" />
            <template #footer v-if="props.type !== 'view'">
                <el-button size="large" @click="onCancel">取 消</el-button>
                <el-button type="primary" size="large" @click="onSubmit">确 定</el-button>
            </template>
        </el-drawer>
    </div>
</template>
