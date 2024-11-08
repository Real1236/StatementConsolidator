from typing import List, Optional
from data_processing_module.statements.consolidated_statement import ConsolidatedStatement
from data_processing_module.statements.statement import Statement
from data_processing_module.statements.transaction import Transaction
from filter import Filter

categoryBank = {
    "PETRO CANADA": "Transportation",
    "TIM HORTONS": "Eating Out",
    "TIMBER CREEK GOLF": "Recreation",
    "VALUE VILLAGE": "Miscellaneous",
    "TEMU.COM": "Shopping",
    "MCDONALD'S": "Eating Out",
    "WENDY'S": "Eating Out",
    "PRESTO AUTO": "Transportation",
    "ADIDAS": "Shopping",
    "GRAND BURRITO": "Eating Out",
    "JACK AND JONES": "Shopping",
    "HOLLISTER": "Shopping",
    "JACK & JONES": "Shopping",
    "COSTCO GAS": "Transportation",
    "A & W": "Eating Out",
    "CINEPLEX": "Recreation",
    "DAIRY QUEEN": "Eating Out",
    "SWISS CHALET": "Eating Out",
    "UNIQLO": "Shopping",
    "UNIONVILLE ARMS PUB": "Eating Out",
    "HUB CLIMBING": "Recreation",
    "KIBO MARKET UNION": "Eating Out",
    "DENNY'S": "Eating Out",
    "LS BUSHWOOD GOLF CLUB": "Recreation",
    "YI FANG TAIWAN FRUIT": "Eating Out",
    "ACTIVATE GAMES": "Recreation",
    "PIE BAR": "Eating Out",
    "PHO QUINN": "Eating Out",
    "GOOD CATCH BAR & CAFE": "Eating Out",
    "BRITISH AIRWAYS": "Transportation",
    "ESSO GAS STATION": "Transportation",
    "ALGONQUIN OUTFITTERS": "Recreation",
    "ONTARIO CANOE TRIP": "Recreation",
    "TOO GOOD TO GO": "Eating Out",
    "ST. LOUIS BAR & GRILL": "Eating Out",
    "SPOTHERO": "Transportation",
    "MAGIC NOODLE": "Eating Out",
    "FRESHCO": "Grocery",
    "TEN REN'S TEA": "Eating Out",
    "LYFT": "Transportation",
}

class Consolidator(Filter):
    def process(self, data: List[Statement]) -> List[Transaction]:
        # Get existing category assignments
        consolidatedStatement = None
        for statement in data:
            if isinstance(statement, ConsolidatedStatement):
                consolidatedStatement = statement
        itemToCategory = self.getCategories(consolidatedStatement) if consolidatedStatement else {}

        # Consolidate and sort transactions from all statements
        transactions: List[Transaction] = []
        transactions_set = set()
        for statement in data:
            for transaction in statement.statement:
                # Remove duplicate transactions and assign categories
                if str(transaction) not in transactions_set:
                    if not transaction.category:
                        if transaction.description1 in itemToCategory:
                            transaction.category = itemToCategory[transaction.description1]
                        else:
                            transaction.category = self.checkCategoryBank(transaction.description1)
                    transactions.append(transaction)
                    transactions_set.add(str(transaction))
                else:
                    if transaction.category or transaction.splitWith:
                        for t in transactions:
                            if str(t) == str(transaction):
                                if transaction.category:
                                    t.category = transaction.category
                                if transaction.splitWith:
                                    t.splitWith = transaction.splitWith
                                break

        transactions.sort(key=lambda x: x.transactionDate)
        return transactions
    
    def getCategories(self, consolidatedStatement: ConsolidatedStatement) -> dict:
        # Get all unique categories from all transactions
        itemToCategory = {}
        for transaction in consolidatedStatement.statement:
            if transaction.category and transaction.description1 != "Email Trfs":
                itemToCategory[transaction.description1] = transaction.category

        return itemToCategory

    def checkCategoryBank(self, description: str) -> Optional[str]:
        for key in categoryBank:
            if key in description:
                return categoryBank[key]
        return None