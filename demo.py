from dotenv import load_dotenv
load_dotenv("./.env")

from openai import OpenAI
import os
from main import run_jury
import time

start = time.time()
models = os.getenv("MODELS").split(",")
print("------------------")
print(f"Connected to {os.getenv('OPENAI_BASE_URL')}")
print(f"Available models: {models}")
print("------------------")

question = "给我讲一个年轻人奋斗创业最终取得成功的故事。"
# gpt-4-turbo
answer_a = """故事的主角是一个叫李华的年轻人。李华出生在一个普通的家庭，他的父母都是普通的工人。尽管家庭条件并不富裕，但他的父母非常重视他的教育，他们希望李华能有一个更好的未来。

在大学毕业后，李华并没有选择像大多数同学那样去大公司工作，而是决定创业。他对科技感兴趣，尤其是人工智能技术。他相信人工智能将会改变世界，所以他决定开设一家人工智能公司。

创业的过程并不容易。在开始的时候，他没有足够的资金，也没有找到合适的团队。然而，李华并没有放弃。他每天都在寻找投资，寻找合适的团队成员。他甚至在晚上也在编写代码，学习人工智能的知识。

经过几年的努力，李华的公司终于取得了一些成果。他们开发的人工智能产品在市场上得到了广泛的认可，公司也开始有了稳定的收入。李华的创业梦想也终于实现了。

李华的故事告诉我们，只要有信心，有毅力，就一定能够实现自己的梦想。创业的过程可能会充满挑战，但只要我们不放弃，就一定能够取得成功。"""
# qwen
answer_b = """故事的主人公名叫杰克，一个充满激情和梦想的年轻人，他出生在一个普通的工薪家庭。自小，杰克就对科技有着浓厚的兴趣，尤其对互联网行业有着独特的见解。他在学校里就展现出了超凡的编程能力和创新思维，常常熬夜研究新的技术，梦想着有一天能用自己的技术改变世界。

大学毕业后，杰克并没有选择像大多数人那样找一份稳定的工作，而是决定创业，创立一家专注于人工智能技术的初创公司。他带着满腔热血，说服了几个志同道合的朋友，他们一起筹集资金，租下了一个小办公室，开始了他们的创业之路。

刚开始的日子异常艰难，资金紧张，团队成员经常加班到深夜，但他们始终保持着对梦想的执着。杰克利用自己的技术专长，开发出一款AI辅助学习软件，帮助学生更有效地掌握知识。尽管市场竞争激烈，但他们凭借软件的实用性和用户体验赢得了用户的口碑，逐渐在市场上站稳了脚跟。

在创业的第五个年头，他们的产品开始受到投资者的关注，获得了一笔风险投资。有了资金的支持，杰克他们扩大了团队，研发出了更多创新产品，如智能客服和数据分析工具，这些产品为企业提供了极大的便利，赢得了更多的客户。

然而，创业路并非一帆风顺。有一次，他们的主要竞争对手推出了类似的产品，几乎要动摇他们的市场地位。杰克没有被压力打倒，他带领团队进行了深度调研，分析市场趋势，最终决定将重心转向AI在医疗领域的应用，开发出一款能够辅助医生进行精准诊断的软件。这次转型，不仅帮助他们抵御了竞争对手，还为公司赢得了新的增长点。

经过十多年的努力，杰克的公司逐渐成为行业领导者，他们的产品被广泛应用于全球，改变了无数人的生活和工作方式。杰克的故事告诉我们，只要有梦想，有毅力，有创新，即使起点低，也能通过不断努力实现创业成功。他的名字和公司成为了业界的典范，激励着更多年轻人勇敢追逐自己的梦想。
"""
def main():
    llm = OpenAI(
        base_url=os.getenv("OPENAI_BASE_URL"),
        api_key=os.getenv("OPENAI_API_KEY")
    )
    results = []
    for model in models:
        result = run_jury(llm, model, question, answer_a, answer_b)
        print(f"Model {model} wins: {result}")
        results.append(result)

        counts = {
        "A": results.count("A"),
        "B": results.count("B"),
        "Tie": results.count("Tie")
    }

    overall_winner = max(counts, key=counts.get)
    if counts["A"] == counts["B"]:
        overall_winner = "Tie"

    print("--------")
    print(f"Overall result: {overall_winner}")
    print(f"Time Taken: {time.time() - start}s")
    print("--------")


if __name__ == '__main__':
    main()