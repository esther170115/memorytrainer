import streamlit as st
import random

st.set_page_config(page_title="数字编码记忆训练", page_icon="🧠")

st.title("🧠 数字编码记忆训练")

# ===== 数据（你可以补全100个）=====
data = {
    "00": "望远镜",
    "01": "小树",
    "02": "铃儿",
    "03": "凳子",
    "04": "轿车",
    "05": "手套",
    "06": "手枪",
    "07": "锄头",
    "08": "溜冰鞋",
    "09": "猫",
    "10": "棒球",
    "11": "楼梯",
    "12": "椅子",
    "13": "医生",
    "14": "钥匙",
    "15": "鹦鹉",
    "16": "石榴",
    "17": "仪器",
    "18": "糖葫芦",
    "19": "衣钩",
    "20": "香烟",
    "21": "鳄鱼",
    "22": "双胞胎",
    "23": "和尚",
    "24": "闹钟",
    "25": "二胡",
    "26": "河流",
    "27": "耳机",
    "28": "婴儿",
    "29": "牢房"
}

# ===== Session状态 =====
if "number" not in st.session_state:
    st.session_state.number = random.choice(list(data.keys()))

# ===== 显示题目 =====
st.subheader("数字：")
st.markdown(f"# {st.session_state.number}")

# ===== 输入 =====
user_input = st.text_input("请输入对应图像")

# ===== 按钮 =====
col1, col2 = st.columns(2)

if col1.button("提交"):
    correct = data[st.session_state.number]
    if user_input == correct:
        st.success("✅ 正确！")
    else:
        st.error(f"❌ 错误，正确答案是：{correct}")

if col2.button("下一题"):
    st.session_state.number = random.choice(list(data.keys()))
    st.rerun()
