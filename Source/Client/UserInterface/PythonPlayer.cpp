/// 1.
// Search
bool CPythonPlayer::IsOpenPrivateShop()
{
	return m_isOpenPrivateShop;
}

// Add below
bool CPythonPlayer::IsDead()
{
	CInstanceBase* pMainInstance = CPythonCharacterManager::Instance().GetMainInstancePtr();
	if (!pMainInstance)
		return false;

	return pMainInstance->IsDead();
}

bool CPythonPlayer::IsPoly()
{
	CInstanceBase* pMainInstance = CPythonCharacterManager::Instance().GetMainInstancePtr();
	if (!pMainInstance)
		return false;

	return pMainInstance->IsPoly();
}
