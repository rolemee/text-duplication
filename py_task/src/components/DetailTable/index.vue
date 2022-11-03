<template>
   <div>
       <el-table
           ref="tableRef"
           highlight-current-row
           :data="pageDate"
           :size="controlSize"
           :style="tableStyle"
           :stripe="props.option.stripe"
           :fit="props.option.fit"
           :height="props.option.tableHeight"
           :border="props.option.border"
           v-loading="dataLoading"
           :table-layout="props.option.tableLayout"
           element-loading-text="数据正在加载中"
           @selection-change="handleSelectionChange"
           @row-click="handleClick"
       >
           <!--增加索引-->
           <el-table-column
               label="序号"
               type="index"
               fixed="left"
               width="60"
               align="center"
           />
           <!--选择框-->
           <el-table-column
               type="selection"
               fixed="left"
               min-width="20"
               align="center"
               v-if="isSelected"
           />
           <!--数据列-->
           <el-table-column
               v-for="(column, index) in props.columns"
               :key="index"
               :sortable="column.sortable"
               :prop="column.prop"
               :label="column.label"
               :align="column.align || 'center'"
               :width="column.width"
               :formatter="column.formatter"
               min-width="50"
           >
               <template #default="scope">
                   <!-- 判断数据列是否为图片 -->
                   <template v-if="column.cellType === 'image'">
                       <el-image
                           style="width: 50px; height: 50px"
                           :src="scope.row.imgSrc"
                           :preview-src-list="[scope.row.imgSrc]"
                           hide-on-click-modal
                           preview-teleported
                       />
                   </template>
                   <!-- 判断数据列是否为Switch开关 -->
                   <template v-else-if="column.cellType === 'switch'">
                       <el-switch
                           v-model="scope.row[column.prop]"
                           size="default"
                           :active-text="myActiveText"
                           :inactive-text="myInactiveText"
                           inline-prompt
                           inactive-color="#ff4949"
                           v-loading="data.switch.loading"
                           @change="onEdit($event,scope.row)"
                       />
                   </template>
                   <!-- 判断数据列是有图标 显示为图标 文字-->
                   <template v-else-if="column.hasOwnProperty('icon')">
                       <div :style="scope.row.color" v-if="column.iconText">
                           <svg-icon :name="column.icon"/>
                           <span>{{scope.row[column.prop]}}</span>
                       </div>
                       <div :style="scope.row.color" v-else>
                           <span>{{scope.row[column.prop]}}</span>
                           <svg-icon :name="column.icon"/>
                       </div>
                   </template>
               </template>
           </el-table-column>
           <el-table-column
               v-if="props.option.operation === true"
               label="操作"
               fixed="right"
               min-width="20"
               align="center"
               :width="props.option.operate.width ||270"
           >
               <template #default="scope" >
                   <el-button v-if='props.option.edit' size="small" plain @click="handleEdit(scope.row)" style="border: none;background-color: inherit;color:#1890ff" >
                       <svg-icon name="ep:edit" />
                       {{props.option.operate.edit || '编辑'}}
                   </el-button>
                   <el-button v-if='props.option.view' type="default" style="border: none;background-color: inherit;color:#1890ff" size="small" plain @click="handleView(scope.row)">
                       <svg-icon name="ep:view" />
                       {{props.option.operate.view || '查看'}}
                   </el-button>
                   <el-dropdown
                       size="small"
                       v-if="props.option.dropdown"
                       @command="handleCommand"
                        trigger="click"
                   >
                       <el-button size="small" style="border: none;background-color: inherit">
                               <span style="font-size: 12px">
                                   {{props.dropdown.title|| '更多操作'}}
                                    <svg-icon name="ep:arrow-down" style="margin-left: 1px"/>
                               </span>
                       </el-button>
                       <template #dropdown>
                           <el-dropdown-menu>
                               <template v-for="(item,index) in props.dropdown.data" :key="index">
                                   <el-dropdown-item :command="{command:item.command, row: scope.row}">
                                       <svg-icon :name="item.name" style="margin-right: 1px"/>
                                       {{item.command}}
                                   </el-dropdown-item>
                               </template>
                           </el-dropdown-menu>
                       </template>
                   </el-dropdown>
               </template>
           </el-table-column>
       </el-table>
       <!--分页-->
       <el-pagination
           v-if="props.option.pagination === true"
           @size-change="handleSizeChange"
           @current-change="handleCurrentChange"
           :current-page="data.pagination.currentPage"
           :page-size="data.pagination.pageSize"
           :page-sizes="data.pagination.pageSizes"
           :total="props.pagination.total"
           background
           :layout=props.pagination.layout
           style="margin-top: 10px"
       />
   </div>
</template>
<script setup >

const props = defineProps({
    tableData: {
        type : Array,
        default : []
    },
    columns: {
        type : Array,
        default: []
    },
    pagination: {
        type : Object,
        default : {
            size: 20,//每页显示的行数
            sizes: [1,2,20, 40, 60, 80, 100],//每页条数
            currentPage: 1, //当前页数
            total: 0,
            layout: 'total, sizes, ->, prev, pager, next, jumper'
        },
    },
    option: {//table样式属性值
        type: Object,
        default: {
            controlSize: null,
            tableStyle: null,
            stripe: true,
            fit: true,
            tableHeight: null,
            isSelected: null,
            border: true,
            pagination: true,
            operation: false,
            dropdown: false,
            edit: true,
            view: true,
            getDataType: 'static'
        }
    },
    dataLoading: {
        type: Boolean,
        default: false
    },
    switch: {
        type: Object,
        default: {
            switchLoading: false,
            activeText: '',
            inactiveText: ''
        }
    },
    dropdown: {
        type: Object,
        default: {
            title: '',
            data: []
        }
    }
})

// onMounted(()=>{
    // console.log(JSON.stringify(props.switch))
    // console.log(data.value.total)
    // console.log(props.option.border)
// })
// onUpdated(() => {
//     console.log(props.pagination)
//     console.log(data.value.pagination)
// })

let $myEmit = defineEmits(
    ['selection-change','switch-change','handleEdit','handleView','handleClick','command',
        'onSizeChange','onCurrentChange']
)

const data =ref({
    dataList: [],
    columns: [],
    pagination: {
        pageSize: props.pagination.size,
        pageSizes: props.pagination.sizes,
        currentPage:  props.pagination.currentPage
    },
    switch: {
        loading: props.switch.switchLoading
    },
    dynamic: props.option.getDataType === 'dynamic'
})

const pageDate = computed({
    get:function(){
        if (props.option.pagination) {
            if (data.value.dynamic) {
                data.value.dataList = props.tableData
            }else {
                data.value.dataList = props.tableData.slice(
                    (data.value.pagination.currentPage - 1) * data.value.pagination.pageSize,
                    data.value.pagination.currentPage * data.value.pagination.pageSize
                )
            }
        }else {
            data.value.dataList = props.tableData
        }
        return data.value.dataList
    },
})

const  controlSize = computed(() => props.option.controlSize || 'small')
const tableStyle = computed(() => props.option.tableStyle || {'width':'100%'})
const dataLoading = computed(() => props.dataLoading || false)
const isSelected = computed(() => props.option.isSelected || false)
const border = computed(() => props.option.border || true)

const myInactiveText = computed(() => props.switch.inactiveText ?? 'false')
const myActiveText = computed(() => props.switch.activeText ?? true )

//获取复选框选中的选项信息
function handleSelectionChange(val){
    // console.log("复选款"+val)
    $myEmit('selection-change',val);
}
//单条点击事件
function handleClick(val){
    $myEmit('handleClick',val)
}

//分页方法
//每页条数
function handleSizeChange(val){
    if (data.value.dynamic)
        $myEmit('onSizeChange', val, () => {
            data.value.pagination.pageSize = props.pagination.size
        })
    else
        data.value.pagination.pageSize = val
}

//当前页
function handleCurrentChange(val){
    if (data.value.dynamic)
        $myEmit('onCurrentChange', val, () => {
            data.value.pagination.currentPage = props.pagination.currentPage
        })
    else
        data.value.pagination.currentPage = val
}

//状态切换
function onEdit(val,row){
    data.value.switch.loading = true
    let value = {
        valid: val,
        row: row
    }
    $myEmit('switch-change',value,() => {
        data.value.switch.loading = false;
    })
}

//编辑操作
function handleEdit(val) {
    $myEmit('handleEdit',val)
}
//查看操作
function handleView(val) {
    $myEmit('handleView',val)
}
//下列表点击
function handleCommand(val) {
    // console.log(JSON.stringify(val))
    $myEmit('command', val)
}
</script>
<style  lang="scss" scoped>
:deep(.el-table th.gutter) {
    /* 解决element-ui 表格篡位的问题 */
    display: table-cell !important;
}
:deep(.el-switch__core) {
    width: 46px;
    .el-switch__inner{
        .is-text {
            font-size: 10px;
        }
    }
}
</style>
