<route>
{
    name: 'dashboard',
    meta: {
        title: "系统说明"
    }
}
</route>

<template>
    <div>
        <page-header title="欢迎使用 Duplicate checking system">
            <template #content>
                <div>
                    <div style="margin-bottom: 5px;">这是一款<b class="text-emphasis">简易</b>好上手、智能、功能强大的查重系统</div>
                    <div>注：此查重系统支持查重c++、java等常见语言编写的程序、word、pdf等各种常见的文本</div>
                </div>
            </template>
        </page-header>
    </div>
</template>

<style lang="scss" scoped>
.text-emphasis {
    text-emphasis-style: "❤";
}
</style>
