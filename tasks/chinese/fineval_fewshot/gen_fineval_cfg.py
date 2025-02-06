"""
Take in a YAML, and output all other splits with this YAML
"""
import argparse
import os

import yaml
from tqdm import tqdm


SUBJECTS = {
    "accounting": "会计",
    "advanced_financial_accounting": "高级财务会计",
    "auditing": "审计学",
    "banking_practitioner_qualification_certificate": "银行从业资格证",
    "central_banking": "中央银行学",
    "certified_management_accountant": "管理会计师",
    "certified_practising_accountant": "注册会计师",
    "china_actuary": "中国精算师",
    "commercial_bank_finance": "商业银行金融学",
    "corporate_finance": "公司金融学",
    "corporate_strategy_and_risk_management": "公司战略与风险管理",
    "cost_accounting": "成本会计学",
    "economic_law": "经济法",
    "econometrics": "计量经济学",
    "finance": "金融学",
    "financial_engineering": "金融工程学",
    "financial_management": "财务管理学",
    "financial_markets": "金融市场学",
    "fund_qualification_certificate": "基金从业资格证",
    "futures_practitioner_qualification_certificate": "期货从业资格证",
    "insurance": "保险学",
    "intermediate_financial_accounting": "中级财务会计",
    "international_economics": "国际经济学",
    "international_finance": "国际金融学",
    "investments": "投资学",
    "macroeconomics": "宏观经济学",
    "management_accounting": "管理会计学",
    "microeconomics": "微观经济学",
    "monetary_finance": "货币金融学",
    "political_economy": "政治经济学",
    "public_finance": "财政学",
    "securities_practitioner_qualification_certificate": "证券从业资格证",
    "statistics": "统计学",
    "tax_law": "税法"
}




def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--base_yaml_path")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    args.base_yaml_path = "tasks/chinese/fineval_fewshot/_default_fineval_yaml"
    # get filename of base_yaml so we can `"include": ` it in our other YAMLs.
    base_yaml_name = os.path.split(args.base_yaml_path)[-1]
    # with open(args.base_yaml_path, encoding="utf-8") as f:
    #     base_yaml = yaml.full_load(f)

    for subject_en, subject_zh in tqdm(SUBJECTS.items()):
        description = f"以下是中国关于{subject_zh}考试的单项选择题，我会给你几个有答案的例子，请你根据最后一个题目的要求进行回答。\n你只需要回答最后一个题目\n\n"

        yaml_dict = {
            "include": f"./{base_yaml_name}",
            "tag": "zh-fineval",
            "task": f"zh-fineval_{subject_en}",
            "dataset_name": subject_en,
            "description": description,
        }

        file_save_path = f"tasks/chinese/fineval_fewshot/{subject_en}.yaml"
        print(f"Saving yaml for subset {subject_en} to {file_save_path}")
        with open(file_save_path, "w", encoding="utf-8") as yaml_file:
            yaml.dump(
                yaml_dict,
                yaml_file,
                width=float("inf"),
                allow_unicode=True,
                default_style='"',
            )
