<template>
    <div style="margin-bottom: 5px">
        <el-button
            v-for="(column,index) in btn"
            :key="index"
            :type="column.type"
            :loading="loading"
            @click="column.even"
            size="small"
            plain
        >
            <svg-icon  :name="column.icon"/>
            {{column.text}}
        </el-button>
    </div>
</template>

<script setup>

const $myEmit = defineEmits(['handleAdd','handleDelete'])
let loading = ref(false)
//操作按钮
const btn = [
    {
        type: 'primary',
        icon: 'ep:plus',
        even: handleAdd,
        text: '新增'
    },
    {
        type: 'danger',
        icon: 'ep:delete',
        even: handleDelete,
        text: '删除'
    }
]
function transfer(str) {
    loading.value = true
    $myEmit(str,null,()=>{
        loading.value = false
    })
}
function  handleAdd() { transfer('handleAdd') }
function  handleDelete() { transfer('handleDelete') }

</script>

<style scoped lang="scss">
//scss
</style>
