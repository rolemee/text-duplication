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


</script>

<template>
    <div>
        <el-dialog v-if="props.mode === 'dialog'" v-model="myVisible" :title="title" width="600px" :close-on-click-modal="false" append-to-body destroy-on-close>
            <DetailForm ref="form" v-bind="$props" />
        </el-dialog>
        <el-drawer v-else-if="props.mode === 'drawer'" v-model="myVisible" :title="title" size="600px" :close-on-click-modal="false" destroy-on-close>
            <DetailForm ref="form" v-bind="$props" />
        </el-drawer>
    </div>
</template>
